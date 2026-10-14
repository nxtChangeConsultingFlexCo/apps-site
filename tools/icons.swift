// Erzeugt die Icons von nxtchange.app aus tools/nxt.png (Schriftzug aus dem nxtChange-Logo):
//
//     assets/apple-touch-icon.png   180 × 180
//     assets/favicon.png             96 × 96
//     favicon.ico                    16, 32, 48
//
//     swift tools/icons.swift
//
// Dunkler Schriftzug, eingraviert in poliertes Gold: hebt das Register vom schwarz-weißen Icon der
// Firmen-Website ab und nimmt den Goldakzent der Seite auf (Entscheidung 14.10.2026).
// Aufbau wie nxt-site/tools/grafik.swift, nur AppKit, keine Abhängigkeiten.
import AppKit

let root = URL(fileURLWithPath: #filePath).deletingLastPathComponent().deletingLastPathComponent()

func color(_ hex: UInt32, alpha: CGFloat = 1) -> NSColor {
    NSColor(srgbRed: CGFloat((hex >> 16) & 0xFF) / 255, green: CGFloat((hex >> 8) & 0xFF) / 255, blue: CGFloat(hex & 0xFF) / 255, alpha: alpha)
}

guard let mark = NSImage(contentsOf: root.appendingPathComponent("tools/nxt.png")) else { fatalError("tools/nxt.png fehlt") }
let markRatio: CGFloat = 208.0 / 391.0

func render(_ width: Int, _ height: Int, _ draw: (CGContext) -> Void) -> NSBitmapImageRep {
    guard let rep = NSBitmapImageRep(bitmapDataPlanes: nil, pixelsWide: width, pixelsHigh: height, bitsPerSample: 8, samplesPerPixel: 4,
                                     hasAlpha: true, isPlanar: false, colorSpaceName: .deviceRGB, bytesPerRow: 0, bitsPerPixel: 0),
          let context = NSGraphicsContext(bitmapImageRep: rep) else { fatalError("Kein Zeichenkontext") }
    rep.size = NSSize(width: width, height: height)
    NSGraphicsContext.saveGraphicsState()
    NSGraphicsContext.current = context
    context.imageInterpolation = .high
    draw(context.cgContext)
    context.flushGraphics()
    NSGraphicsContext.restoreGraphicsState()
    return rep
}

// Zeichnet den Schriftzug in einer Farbe: erst das Bild, dann die Farbe nur dort, wo das Bild deckt.
func drawMark(in rect: NSRect, color: NSColor, context: CGContext) {
    context.saveGState()
    context.beginTransparencyLayer(auxiliaryInfo: nil)
    mark.draw(in: rect, from: .zero, operation: .sourceOver, fraction: 1)
    context.setBlendMode(.sourceIn)
    context.setFillColor(color.cgColor)
    context.fill(rect)
    context.endTransparencyLayer()
    context.restoreGState()
}

func write(_ data: Data, _ path: String, _ note: String) {
    do { try data.write(to: root.appendingPathComponent(path)) } catch { fatalError("\(path): \(error)") }
    print("\(path): \(data.count) bytes, \(note)")
}

// Favicons sind gerundet wie bei nxt-site (20 %). Das Touch-Icon bleibt eckig und deckend, iOS rundet es selbst (etwa 22,4 %);
// die Lichtkante folgt dieser Rundung.
func icon(_ size: Int, rounded: Bool) -> Data {
    let rep = render(size, size) { context in
        let side = CGFloat(size)
        let square = NSRect(x: 0, y: 0, width: side, height: side)
        let radius = side * (rounded ? 0.2 : 0.224)
        if rounded { NSBezierPath(roundedRect: square, xRadius: radius, yRadius: radius).addClip() }
        // Poliertes Gold: diagonal hell, satt, tief, wieder hell, wie Licht auf gewölbtem Metall.
        NSGradient(colorsAndLocations: (color(0xF6E9C4), 0), (color(0xDCC693), 0.3), (color(0xAE9260), 0.58), (color(0xD8C18E), 0.82), (color(0xEBDAAC), 1))?
            .draw(in: square, angle: -45)
        let w = side * (size <= 48 ? 0.84 : 0.72), h = w * markRatio
        let markRect = NSRect(x: (side - w) / 2, y: (side - h) / 2, width: w, height: h)
        // Lichtkante am Rand und helle Kante unter dem Schnitt der Gravur; bis 48 Pixel verschwimmen beide und bleiben weg.
        if size > 48 {
            let inset = side * 0.01
            let rim = NSBezierPath(roundedRect: square.insetBy(dx: inset, dy: inset), xRadius: radius - inset, yRadius: radius - inset)
            rim.lineWidth = side * 0.02
            color(0xFFFFFF, alpha: 0.35).setStroke()
            rim.stroke()
            drawMark(in: markRect.offsetBy(dx: 0, dy: -side * 0.012), color: color(0xFFF6DC, alpha: 0.75), context: context)
        }
        drawMark(in: markRect, color: color(0x2A1F10), context: context)
    }
    guard let png = rep.representation(using: .png, properties: [:]) else { fatalError("PNG fehlgeschlagen") }
    return png
}

write(icon(180, rounded: false), "assets/apple-touch-icon.png", "180 × 180")
write(icon(96, rounded: true), "assets/favicon.png", "96 × 96")

// favicon.ico: Kopf (6 Bytes), je Größe ein Verzeichniseintrag (16 Bytes), dahinter die PNG-Daten.
func le16(_ value: Int) -> [UInt8] { [UInt8(value & 0xFF), UInt8((value >> 8) & 0xFF)] }
func le32(_ value: Int) -> [UInt8] { le16(value & 0xFFFF) + le16((value >> 16) & 0xFFFF) }
let sizes = [16, 32, 48]
let images = sizes.map { icon($0, rounded: true) }
var ico = Data(le16(0) + le16(1) + le16(sizes.count))
var offset = 6 + 16 * sizes.count
for (size, image) in zip(sizes, images) {
    ico.append(contentsOf: [UInt8(size), UInt8(size), 0, 0] + le16(1) + le16(32) + le32(image.count) + le32(offset))
    offset += image.count
}
images.forEach { ico.append($0) }
write(ico, "favicon.ico", sizes.map(String.init).joined(separator: ", "))
