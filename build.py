#!/usr/bin/env python3
"""
build.py — generates the ADSD Steel Technical Services Contracting L.L.C site.

All company facts (services, projects, licences, contact details) are taken
verbatim from ADSD-COMPANY-PROFILE_-_Steel_Structure.pdf. Anything the profile
did not contain is written as industry-appropriate placeholder copy and listed
in CONTENT-NOTES.md.
"""
import os, json, html, shutil

OUT = 'site'
SITE = 'https://www.adsdsteel.ae'          # <- replace with the live domain

CO      = 'ADSD Steel Technical Services Contracting L.L.C'
CO_SHORT= 'ADSD Steel'
PHONE   = '+971 56 996 8611'
PHONE_H = '+971569968611'
WA      = PHONE_H.replace('+', '')
EMAIL   = 'ads.techdxb@gmail.com'
POBOX   = 'P.O. Box 282615, Dubai, UAE'
TRN     = '104023207400003'
LIC_DXB = '1050680'
LIC_SHJ = '502971'

NAV = [
    ('About',      '#about'),
    ('Capability', '#capability'),
    ('Products',   '#products'),
    ('Projects',   '#projects'),
    ('Gallery',    'gallery.html'),
    ('Contact',    '#contact'),
]

# ---------------------------------------------------------------- services --
SERVICES = [
    dict(
        slug='structural-steel-fabrication',
        title='Structural Steel Fabrication &amp; Installation',
        plain='Structural Steel Fabrication and Installation',
        short='Primary frames, secondary steel and connections — cut, drilled, welded and erected to approved shop drawings.',
        hero='portal-frame-erection',
        lead='Primary and secondary structural steel, fabricated in our own workshop and erected on site by our own crews — from setting-out to final bolt-up.',
        body=[
            'Structural steel is the discipline the company was built on. Work starts from your design drawings, which we develop into shop drawings for approval before a single section is cut. Members are marked, cut, drilled, fitted and welded in the workshop, finished to the specified coating system, then delivered to site in erection sequence.',
            'On site the same team sets out from the column grid, plumbs and levels the frame, torques the connections and hands over a surveyed structure with as-built marks that match the drawings. Because fabrication and erection sit under one roof, drawing queries, fit-up corrections and site changes are resolved without passing between companies.',
        ],
        features=[
            ('Shop drawings and take-off', 'Member marks, connection details, bolt lists and cutting schedules developed from your design drawings and issued for approval.'),
            ('Cutting, drilling and fitting', 'Beams, columns, plates and hollow sections prepared to length, with holes and cleats set out from the same marked drawing.'),
            ('Welding to procedure', 'Fillet and butt welds carried out by trade-tested welders working to an agreed procedure and visual acceptance criteria.'),
            ('Surface treatment', 'Blast or mechanical preparation followed by the specified primer and finish, or hot-dip galvanising through approved applicators.'),
            ('Delivery in erection sequence', 'Loads batched frame by frame so the crane lifts in the order the crew needs them, not in the order the workshop finished them.'),
            ('Erection, alignment and bolt-up', 'Setting-out from the column grid, plumbing and levelling, permanent bracing, torqued connections and a surveyed handover.'),
        ],
        benefits=[
            ('One accountable party', 'The crew that welds the connection is the crew that bolts it up, so fit-up problems are corrected rather than argued over.'),
            ('Fewer drawing loops', 'Shop drawings are produced against the same take-off used for procurement, which keeps revisions and re-cuts down.'),
            ('Predictable site programme', 'Deliveries follow the erection sequence, so lifting plant is not standing idle waiting for the right member.'),
            ('Records that match the steel', 'Member marks, bolt grades and coating details are recorded as built and handed over with the structure.'),
        ],
        specs=[
            ('Structure types', 'Portal frames, multi-storey frames, mezzanines, pipe racks, platforms, support steel'),
            ('Sections handled', 'Universal beams and columns, channels, angles, plate girders, hollow sections, built-up members'),
            ('Connections', 'Bolted connections to structural grade, site welding where the design calls for it'),
            ('Finishes', 'Shop primer, two-pack systems, intumescent through applicators, hot-dip galvanising'),
            ('Scope options', 'Supply and fix, fabrication only, erection only, or labour and supervision'),
            ('Coverage', 'Dubai, Sharjah, Abu Dhabi and the Northern Emirates'),
        ],
        gallery=['ssf-rooftop-screen-ladder', 'ssf-canopy-entrance', 'ssf-cantilever-walkway',
                 'ssf-stair-balustrade', 'ssf-cnc-screen-wall'],
    ),
    dict(
        slug='miscellaneous-metal-works',
        title='Miscellaneous Metal Works',
        plain='Miscellaneous Metal Work',
        short='Handrails, ladders, aluminium louvers, car parking sheds and substation chequer plate — the finishing steel.',
        hero='laser-metal-cutting',
        lead='The secondary metalwork that finishes a building: handrails, aluminium louvers, car parking sheds, substation chequer plate, ladders, gates and brackets.',
        body=[
            'The company profile groups this work as miscellaneous metal work, and it is usually the scope that decides whether a project feels finished. It is measured on site rather than scaled off a drawing, because openings, floor levels and kerb lines are never exactly where the design put them.',
            'Typical items include handrails and balustrades, aluminium louvers and screens, car parking sheds and canopies, substation chequer plate and access covers, cage ladders, gates, frames, grating and support brackets — fabricated to the measured dimension and installed by the same team.',
        ],
        features=[
            ('Handrails and balustrades', 'Tubular and section handrails, mid-rails, kick plates and stanchions to stair, platform and edge conditions.'),
            ('Aluminium louvers and screens', 'Weather and privacy louvers, plant screens and enclosures in aluminium and coated steel.'),
            ('Car parking sheds', 'Steel-framed shade structures and canopies with the specified membrane or sheet covering.'),
            ('Substation chequer plate', 'Chequer plate flooring, trench covers and access panels for substations and plant rooms.'),
            ('Ladders and access', 'Cage ladders, step-overs, grating walkways and small platforms.'),
            ('Gates, frames and brackets', 'Doors, gates, frames, bollards and support brackets fabricated to a site-measured dimension.'),
        ],
        benefits=[
            ('Measured, not assumed', 'Every item is set out from a site measurement, which is why it fits first time.'),
            ('Finishes that survive the Gulf', 'Galvanising and powder coating specified for coastal and industrial exposure.'),
            ('Snag-list scope handled', 'The small awkward items that hold up handover are covered rather than deferred.'),
            ('Matched to the main steel', 'Secondary metalwork is detailed to sit correctly against the primary frame we fabricated.'),
        ],
        specs=[
            ('Handrails', 'Tubular and section systems, galvanised or painted, to stair and edge protection requirements'),
            ('Louvers', 'Aluminium and coated-steel weather, privacy and plant screening louvers'),
            ('Shade structures', 'Steel-framed car parking sheds, walkway canopies, entrance canopies'),
            ('Flooring', 'Chequer plate, open grating, trench and pit covers'),
            ('Finishes', 'Hot-dip galvanised, powder coated, two-pack painted, mill finish aluminium'),
            ('Basis', 'Site-measured fabrication, delivered and installed by our own crews'),
        ],
        gallery=['mmw-glass-marble-staircase', 'mmw-brass-room-divider', 'mmw-laser-cut-ceiling-trim',
                 'mmw-acp-signage-panel', 'mmw-stained-glass-staircase', 'mmw-gold-mirror-trim',
                 'mmw-fabricated-rack-frame', 'mmw-stainless-step-stool', 'mmw-floor-drain-grate',
                 'mmw-slot-drain-grate', 'mmw-recessed-floor-drain', 'mmw-commercial-kitchen-counter',
                 'mmw-outdoor-kitchen-cabinet', 'mmw-recessed-wash-trough', 'mmw-walkin-pantry-shelving',
                 'mmw-decorative-bollard', 'mmw-tv-feature-wall', 'mmw-island-cooking-range',
                 'mmw-outdoor-sink-bbq-combo', 'mmw-tandoori-oven-unit', 'mmw-fish-display-counter',
                 'mmw-display-cabinet-gold', 'mmw-gold-slatted-shelving'],
    ),
    dict(
        slug='tailor-made-fabrication-civil',
        title='Tailor-Made Fabrication Products for the Civil Sector',
        plain='Tailor-Made Fabrication Products for the Civil Sector',
        short='Custom-fabricated steelwork engineered to the civil drawing — embedments, temporary works and site-specific metalwork made to order.',
        hero='structure-under-erection',
        lead='Steel fabricated to the exact dimension a civil scope calls for — embedments, temporary works and access steel made to your drawing, not picked off a standard range.',
        body=[
            'Civil works rarely fit a catalogue item. Foundations, grade beams, embedments and site conditions are different on every project, so we fabricate to the drawing and the site measurement rather than asking a civil contractor to design around stock sizes.',
            'From embedded plates and cast-in items through to temporary works steel, access platforms and site railings, the same workshop that fabricates our structural frames turns civil-specific requests around against your programme, with drawings developed and approved before cutting starts.',
        ],
        features=[
            ('Embedded and cast-in steel', 'Base plates, anchor cages and embedment items detailed to the civil drawing and delivered ahead of the pour.'),
            ('Temporary works steel', 'Props, bracing, formwork support and lifting frames fabricated to the design issued by the engineer.'),
            ('Access and edge protection', 'Site railings, guardrails and edge protection fabricated to fit the actual excavation or slab edge.'),
            ('Site-measured brackets', 'One-off brackets, supports and fixings made to a site dimension rather than a standard size.'),
            ('Shop drawings on request', 'Detail drawings produced from your design intent and issued for approval before fabrication.'),
            ('Fast turnaround', 'Civil programmes move quickly, so urgent items are prioritised through the workshop.'),
        ],
        benefits=[
            ('Made to the drawing, not the catalogue', 'Every item is fabricated to the actual dimension, so it fits without site modification.'),
            ('One workshop, any quantity', 'From a single embedment plate to a full package of temporary works steel.'),
            ('Keeps the pour on programme', 'Cast-in and embedded items are delivered ahead of the concrete date, not chasing it.'),
            ('Direct from the fabricator', 'No middleman mark-up between the drawing and the steel — priced and made in-house.'),
        ],
        specs=[
            ('Typical items', 'Embedded plates, anchor cages, temporary works steel, site railings, brackets'),
            ('Materials', 'Mild steel, galvanised steel, stainless steel on request'),
            ('Basis', 'Civil and structural drawings, site measurement, or the engineer design issued for the works'),
            ('Finishes', 'Primer, galvanised, or mill finish as specified'),
            ('Lead times', 'Prioritised against civil pour and programme dates'),
            ('Scope options', 'Supply only, or supply and fix on site'),
        ],
        gallery=['structure-under-erection', 'site-warehouse-build', 'structure-crane-lift', 'steel-cutting'],
    ),
    dict(
        slug='tailor-made-fabrication-mep',
        title='Tailor-Made Fabrication Products for the MEP Sector',
        plain='Tailor-Made Fabrication Products for the MEP Sector',
        short='Custom steel supports, platforms and brackets fabricated to suit mechanical, electrical and plumbing installations.',
        hero='process-platform-steel',
        lead='Supports, platforms and brackets fabricated to fit the equipment, ductwork and containment an MEP contractor is actually installing — not a generic bracket range.',
        body=[
            'MEP installations carry steel that is rarely off the shelf: plant supports, duct hangers, cable tray ladder racks, pipe bridges and equipment platforms all need to match a specific layout. We fabricate these to your coordinated drawing, so the support is right the first time it reaches site.',
            'Because the same workshop cuts, drills and welds every piece, changes that come out of a coordination meeting can be turned around quickly — a revised bracket or an extra hanger does not have to wait behind a large order.',
        ],
        features=[
            ('Plant and equipment supports', 'Steel stands, cradles and frames fabricated to suit chillers, AHUs, pumps and packaged plant.'),
            ('Duct and cable tray supports', 'Hangers, trapezes and brackets sized to the coordinated services drawing.'),
            ('Pipe bridges and racks', 'Support steel for MEP pipe routes crossing plant rooms, risers and roof levels.'),
            ('Access platforms', 'Maintenance platforms and walkways built around plant that needs to stay serviceable.'),
            ('Builders work coordination', 'Support steel detailed to coordinate with builders work openings and civil elements.'),
            ('Quick-turn revisions', 'Late coordination changes are fabricated and delivered without holding up the wider package.'),
        ],
        benefits=[
            ('Fits the coordinated drawing', 'Supports are made to the services layout as coordinated, not a standard span table.'),
            ('One point of contact', 'Mechanical, electrical and plumbing support steel comes from a single fabricator.'),
            ('Responsive to site changes', 'Coordination revisions are turned around from the same workshop, not re-ordered from scratch.'),
            ('Finished for the environment', 'Coatings specified for plant rooms, roof exposure or corrosive environments as needed.'),
        ],
        specs=[
            ('Typical items', 'Plant stands, duct and pipe hangers, cable tray supports, access platforms'),
            ('Materials', 'Mild steel, galvanised steel, stainless steel on request'),
            ('Basis', 'Coordinated MEP shop drawings or site survey'),
            ('Finishes', 'Galvanised, powder coated, or primer and paint as specified'),
            ('Coordination', 'Builders work and clash coordination with the wider MEP package'),
            ('Scope options', 'Supply only, or supply and install on site'),
        ],
        gallery=['process-platform-steel', 'plant-steel-structure', 'silo-platform-access', 'tank-platform-crane'],
    ),
    dict(
        slug='tailor-made-fabrication-landscape-hospitality',
        title='Tailor-Made Fabrication Products for the Landscape &amp; Hospitality Industry',
        plain='Tailor-Made Fabrication Products for the Landscape and Hospitality Industry',
        short='Custom steel pergolas, shade structures and outdoor metalwork fabricated for landscape and hospitality projects.',
        hero='canopy-steel-frame',
        lead='Pergolas, shade structures and outdoor metalwork fabricated to a landscape or hospitality design intent, built to hold a finish as well as a load.',
        body=[
            'Landscape and hospitality work is judged on appearance as much as strength, so fabrication is set out from the design drawing issued by the architect or landscape designer, with attention to clean welds, consistent radii and a finish that will be seen up close.',
            'From pergolas and shade canopies to planters, screens and outdoor furniture frames, pieces are fabricated in the workshop and finished before delivery, so installation on a live landscape or hospitality site is fast and clean.',
        ],
        features=[
            ('Pergolas and shade structures', 'Steel-framed pergolas and shade canopies fabricated to the landscape design.'),
            ('Planters and screens', 'Custom planter boxes, privacy screens and decorative metalwork to a specified profile.'),
            ('Outdoor furniture frames', 'Steel frames for benches, loungers and fixed furniture built for outdoor use.'),
            ('Feature and decorative steel', 'Architectural metalwork where the weld line and finish are part of the design.'),
            ('Weather-ready finishes', 'Galvanising and powder coating specified for sun, humidity and coastal exposure.'),
            ('Coordinated installation', 'Delivered and fixed to suit the landscaping or hospitality fit-out programme.'),
        ],
        benefits=[
            ('Built to the design, not a catalogue', 'Every piece is fabricated to the drawing issued by the architect or designer.'),
            ('Finish-first fabrication', 'Welds, edges and coatings are finished to be seen, not just to hold load.'),
            ('One workshop for the whole package', 'Pergolas, screens, planters and furniture frames from a single supplier.'),
            ('Durable in the Gulf climate', 'Coatings specified to survive sun, humidity and coastal exposure.'),
        ],
        specs=[
            ('Typical items', 'Pergolas, shade canopies, planters, screens, outdoor furniture frames'),
            ('Materials', 'Mild steel, galvanised steel, aluminium on request'),
            ('Basis', 'Architect or landscape design drawings, or a supplied concept'),
            ('Finishes', 'Hot-dip galvanised, powder coated, feature paint finishes'),
            ('Sectors', 'Landscaping contractors, hotels, resorts, leisure and F&amp;B fit-outs'),
            ('Scope options', 'Supply only, or supply and install on site'),
        ],
        gallery=['canopy-steel-frame', 'car-parking-shade-row', 'car-parking-shade-single', 'open-shed-structure'],
    ),
]

# ---------------------------------------------------------------- products --
PRODUCTS = [
    dict(
        slug='pre-engineered-steel-buildings',
        title='Pre-Engineered Steel Buildings',
        tag='Structures',
        short='Clear-span warehouses, workshops and industrial sheds — frames fabricated, clad and erected as one package.',
        hero='warehouse-exterior',
        lead='Clear-span portal-frame buildings for warehousing, workshops and light industry — engineered, fabricated, clad and erected as a single package.',
        overview=[
            'A pre-engineered building is the most efficient way to get covered industrial space onto a plot. The frame is designed around your required clear span and eaves height, fabricated as marked members in our workshop, then bolted together on site in a fraction of the time an in-situ structure would take.',
            'We supply the whole envelope: primary frames, purlins and side rails, bracing, roof and wall sheeting, insulation, gutters and downpipes, and the openings — roller shutters, personnel doors, louvers and translucent roof lights. Mezzanine floors, crane gantries and office fit-out steel can be built into the same frame from the outset.',
        ],
        benefits=[
            ('Faster to close in', 'Bolted portal frames erect in days, not the weeks an in-situ structure needs, so the building is weathertight sooner.'),
            ('One package, one contract', 'Frame, envelope and openings come from the same crew, so there is no gap between who built it and who clads it.'),
            ('Built for expansion', 'Mezzanines, crane gantries and bays designed into the frame from the outset, not retrofitted later.'),
            ('Engineered to your span', 'Sized around the clear span and eaves height you actually need, not a standard catalogue module.'),
        ],
        features=[
            ('Clear-span portal frames', 'Column and rafter frames sized to your span and eaves height, with haunches detailed for the applied loading.'),
            ('Secondary steel', 'Purlins, side rails, eave beams, ridge members and full bracing sets, marked to the erection drawing.'),
            ('Roof and wall envelope', 'Single-skin or insulated panel sheeting with flashings, gutters, downpipes and closures.'),
            ('Openings', 'Roller shutters, sliding and personnel doors, louvers, ventilators and translucent roof lights.'),
            ('Built-in extras', 'Mezzanine floors, crane gantry beams, canopies and office steel designed into the frame.'),
            ('Erection by our crews', 'Setting-out, lifting, plumbing, bolt-up and sheeting carried out by the team that fabricated the steel.'),
        ],
        specs=[
            ('Typical clear spans', 'Single and multi-bay configurations to suit the plot and required column-free area'),
            ('Frame type', 'Bolted portal frames with haunched knee and apex connections'),
            ('Secondary steel', 'Cold-formed purlins and side rails, rod and angle bracing'),
            ('Cladding', 'Single-skin profiled sheet or insulated sandwich panel'),
            ('Openings', 'Roller shutters, sliding doors, personnel doors, louvers, roof lights'),
            ('Finishes', 'Shop-primed and painted steel, or hot-dip galvanised secondary members'),
            ('Options', 'Mezzanine floors, crane gantries, canopies, office and ablution blocks'),
            ('Basis', 'Supply and erect, or supply only for erection by your own crew'),
        ],
        gallery=['warehouse-exterior', 'portal-frame-erection', 'open-shed-structure', 'completed-warehouse',
                 'curved-roof-erection', 'warehouse-interior-lighting'],
    ),
    dict(
        slug='car-parking-shades',
        title='Car Parking Shades &amp; Canopies',
        tag='Shade structures',
        short='Steel-framed parking shades, walkway covers and entrance canopies built for UAE sun and wind loading.',
        hero='car-parking-shade-row',
        lead='Steel-framed shade structures for car parks, walkways and entrances — engineered for UAE sun, wind uplift and a finish that survives a coastal summer.',
        overview=[
            'Parking shades take more punishment than most people expect: forty-plus degrees of daily thermal cycling, wind uplift that tries to peel the covering off, and airborne salt working on every fixing. The frame therefore matters more than the fabric.',
            'We fabricate cantilever, single-post and back-to-back frames from hollow sections and plate, hot-dip galvanise or powder coat them, and set them on cast-in or post-installed base plates surveyed to the parking layout. The covering can be tensioned membrane, profiled sheet or insulated panel depending on the look, the budget and the maintenance you want to sign up for.',
        ],
        benefits=[
            ('Engineered for the uplift case', 'Sized for the wind load that actually fails Gulf shade structures, not just the dead weight.'),
            ('Finish that survives a coastal summer', 'Hot-dip galvanised or powder coated steelwork specified for salt and UV exposure.'),
            ('Bays stay usable', 'Bases set out against the surveyed parking layout, not the drawing, so columns land where cars actually park.'),
            ('Covering to match the budget', 'Tensioned membrane, profiled sheet or insulated panel — whichever suits the look and the maintenance you want.'),
        ],
        features=[
            ('Frame configurations', 'Cantilever, single-post, double-cantilever and back-to-back arrangements to suit the bay layout.'),
            ('Engineered for wind uplift', 'Members, bases and fixings sized for the uplift case, which is what fails first in the Gulf.'),
            ('Covering options', 'Tensioned PVDF or HDPE membrane, profiled steel sheet, or insulated sandwich panel.'),
            ('Durable finishes', 'Hot-dip galvanised or powder coated steelwork specified for coastal exposure.'),
            ('Drainage detailing', 'Gutters, downpipes and fall arranged so water leaves the structure rather than the car.'),
            ('Surveyed setting-out', 'Bases set out against the marked parking layout so bays remain usable after installation.'),
        ],
        specs=[
            ('Configurations', 'Cantilever, single-post, back-to-back, walkway and entrance canopies'),
            ('Frame material', 'Structural hollow sections and plate'),
            ('Finishes', 'Hot-dip galvanised, polyester powder coated, two-pack painted'),
            ('Coverings', 'Tensioned membrane (PVDF / HDPE), profiled steel sheet, insulated panel'),
            ('Fixing', 'Cast-in holding-down bolts or post-installed chemical anchors'),
            ('Drainage', 'Integral gutters and concealed or external downpipes'),
            ('Applications', 'Staff and visitor car parks, labour accommodation, schools, industrial yards, walkways'),
            ('Basis', 'Design, supply and install; membrane replacement on existing frames'),
        ],
        gallery=['car-parking-shade-row', 'car-parking-shade-single', 'canopy-steel-frame', 'open-shed-structure',
                 'louver-screen-enclosure', 'clad-warehouse-green'],
    ),
    dict(
        slug='handrails-ladders-balustrades',
        title='Handrails, Ladders &amp; Balustrades',
        tag='Access &amp; safety',
        short='Edge protection, stair handrails, cage ladders and platform balustrades fabricated to site-measured dimensions.',
        hero='hlb-tubular-stair-handrail',
        lead='Edge protection and access metalwork — stair handrails, platform balustrades, cage ladders and step-overs, fabricated to a site measurement so they fit first time.',
        overview=[
            'Handrails and ladders are safety items, and they are also the last thing installed before an inspection. Both facts argue for measuring the actual structure rather than scaling the drawing: slab edges move, stair rises get adjusted, and a rail fabricated to the design dimension often arrives 30 mm short.',
            'We measure on site, fabricate to that dimension, and install with the fixings the substrate actually needs. Systems are available in galvanised tube, painted section, stainless steel and aluminium, with mid-rails, kick plates and infill panels to suit the exposure and the specification.',
        ],
        benefits=[
            ('Measured, not assumed', 'Every run is set out from the as-built structure, which is why it fits first time.'),
            ('Passes inspection first time', 'Fabricated as a safety item to the standard the inspector is actually checking against.'),
            ('Substrate-correct fixing', 'Base plates and anchors selected for the concrete or steel actually being fixed into.'),
            ('Matched to the main steel', 'Detailed to sit correctly against the primary frame, since we fabricated that too.'),
        ],
        features=[
            ('Stair and landing handrails', 'Stringer-mounted and floor-mounted rails with returns, wall brackets and continuous top rails.'),
            ('Platform balustrades', 'Stanchions, mid-rails and kick plates to platform and roof edge conditions.'),
            ('Cage ladders and step-overs', 'Vertical ladders with hoops and safety cages, plus step-over stiles for pipe and duct routes.'),
            ('Infill options', 'Vertical bar, mesh, perforated sheet and glass-ready channel where the specification calls for it.'),
            ('Site-measured fabrication', 'Every run set out from a measured survey rather than the design dimension.'),
            ('Substrate-correct fixing', 'Base plates, side fixings and chemical anchors selected for the concrete or steel being fixed into.'),
        ],
        specs=[
            ('Materials', 'Galvanised steel tube, structural section, stainless steel, aluminium'),
            ('Finishes', 'Hot-dip galvanised, powder coated, two-pack painted, mill or brushed stainless'),
            ('Configurations', 'Stair rails, landing rails, platform balustrades, roof edge protection'),
            ('Ladders', 'Vertical cage ladders, step-overs, access platforms'),
            ('Infill', 'Vertical bars, mesh, perforated sheet, kick plates'),
            ('Fixing', 'Base-plated, side-fixed or cast-in, with chemical anchors where required'),
            ('Basis', 'Site survey, fabrication and installation by our own crews'),
            ('Typical use', 'Plant platforms, stairs, mezzanines, roof access, substations'),
        ],
        gallery=['hlb-wall-mounted-handrail', 'hlb-tubular-stair-handrail', 'hlb-circular-baluster-handrail',
                 'hlb-pool-handrail', 'hlb-ramp-handrail'],
    ),
    dict(
        slug='aluminium-louvers-screens',
        title='Aluminium Louvers &amp; Screens',
        tag='Facade &amp; screening',
        short='Weather louvers, privacy screens and plant enclosures in aluminium and coated steel, made to opening size.',
        hero='louver-screen-corner',
        lead='Weather louvers, privacy screens and plant enclosures — made to the measured opening, in aluminium or coated steel, with a bird mesh and a drainage detail that works.',
        overview=[
            'Louvers do two jobs at once: let air through and keep weather out. Getting both right is a matter of blade profile, pitch and the drainage path behind the blade — which is why an off-the-shelf panel cut down to size on site usually leaks.',
            'We fabricate louver panels and screens to the measured opening, with the frame, blades, mesh and flashing detailed as one assembly. Applications range from generator and chiller enclosures to substation ventilation, plant screening on roofs, and privacy screens on facades and balconies.',
        ],
        benefits=[
            ("Doesn't leak", 'Blade pitch and drainage path detailed as one assembly, not a panel cut down on site and hoped for.'),
            ('Made to the opening, not a standard size', 'Fabricated to the measured opening with the flashings built into the assembly.'),
            ('Mesh you don\'t see', 'Bird and insect mesh fitted within the frame rather than tacked over the face.'),
            ('Serviceable behind the screen', 'Removable and hinged panels provided where the plant behind needs access.'),
        ],
        features=[
            ('Weather louvers', 'Blade profile and pitch selected for the required free area and rain defence.'),
            ('Privacy and screening panels', 'Fixed blade, vertical fin and perforated screens for facades, roofs and balconies.'),
            ('Plant enclosures', 'Louvered enclosures for generators, chillers, pumps and substation ventilation.'),
            ('Made to opening size', 'Panels fabricated to the measured opening with the flashings detailed as part of the assembly.'),
            ('Bird and insect mesh', 'Rear mesh fitted within the frame rather than fixed over the face.'),
            ('Access provision', 'Removable panels, hinged doors and lifting points where equipment behind needs servicing.'),
        ],
        specs=[
            ('Materials', 'Extruded aluminium, aluminium sheet, coated steel'),
            ('Finishes', 'Powder coated to RAL, anodised, mill finish, PVDF for high exposure'),
            ('Blade types', 'Fixed weather blade, chevron, vertical fin, perforated panel'),
            ('Mesh', 'Aluminium or stainless bird and insect mesh within the frame'),
            ('Frames', 'Aluminium or galvanised steel sub-frames with flashings and closures'),
            ('Access', 'Removable and hinged panels with lifting or handle provision'),
            ('Applications', 'Generator and chiller enclosures, substations, roof plant screening, facades'),
            ('Basis', 'Site survey, fabrication and installation'),
        ],
        gallery=['louver-screen-corner', 'louver-screen-enclosure', 'cladding-blue-facade', 'cladding-panel-wall',
                 'clad-warehouse-green', 'completed-warehouse'],
    ),
    dict(
        slug='chequer-plate-platforms',
        title='Chequer Plate &amp; Access Platforms',
        tag='Flooring &amp; platforms',
        short='Substation chequer plate, trench covers, grating walkways and maintenance platforms built to the opening.',
        hero='silo-platform-access',
        lead='Chequer plate flooring, trench and pit covers, grating walkways and maintenance platforms — cut to the opening, framed, and safe to stand on.',
        overview=[
            'Substation chequer plate is named in the company profile because it is a scope that gets ordered late and needed urgently. It is also unforgiving: a cover that rocks, a plate that deflects under load, or a lifting point that has corroded shut is a hazard, not a detail.',
            'We fabricate chequer plate and grating flooring against the measured opening, with framing, stiffeners, seatings and lifting provision designed for the imposed load and the way the panel will actually be lifted. The same fabrication covers maintenance platforms, walkways and step-overs around plant.',
        ],
        benefits=[
            ('Load-checked, not standard-detail', 'Framing and stiffeners are sized from the stated imposed load, not a generic table.'),
            ('Lifting points that still work', 'Recessed keys and eyes detailed to survive a year outdoors, not seize shut.'),
            ('No rocking covers', 'Seatings and stops set out from the measured opening so panels sit flush.'),
            ('Fast turnaround on urgent orders', 'Fabricated against the scope that typically gets ordered late and needed immediately.'),
        ],
        features=[
            ('Substation chequer plate', 'Floor plate, trench covers and access panels framed and stiffened for the imposed load.'),
            ('Trench and pit covers', 'Removable panels with seatings, stops and recessed lifting keys.'),
            ('Grating walkways', 'Open-mesh grating panels with clips, nosings and edge trims.'),
            ('Maintenance platforms', 'Framed platforms with handrails, kick plates and stair or ladder access.'),
            ('Load-checked framing', 'Bearer sizes and stiffeners set from the stated imposed load rather than a standard detail.'),
            ('Lifting provision', 'Recessed keys, lifting eyes and handles that still work after a year outdoors.'),
        ],
        specs=[
            ('Plate', 'Raised-pattern chequer plate in the specified thickness'),
            ('Grating', 'Open-mesh steel grating with clips and nosings'),
            ('Framing', 'Angle and channel frames, bearers, stiffeners, seatings'),
            ('Finishes', 'Hot-dip galvanised or painted to the specified system'),
            ('Access provision', 'Recessed lifting keys, lifting eyes, handles, hinged panels'),
            ('Edge protection', 'Handrails, kick plates and toe boards where the platform requires them'),
            ('Applications', 'Substations, plant rooms, pump pits, cable trenches, maintenance access'),
            ('Basis', 'Site measurement, fabrication and installation'),
        ],
        gallery=['cpp-recessed-cover-tray', 'cpp-access-hatch-door', 'cpp-floor-grate-vent',
                 'cpp-chequer-plate-cover', 'cpp-stacked-floor-covers', 'cpp-channel-grating',
                 'cpp-heavy-duty-manhole', 'cpp-roof-hatch-cover', 'cpp-linear-slot-drain',
                 'cpp-rain-water-outlet'],
    ),
    dict(
        slug='cladding-roofing-systems',
        title='Cladding &amp; Roofing Systems',
        tag='Building envelope',
        short='Profiled sheet and insulated panel roofing, wall cladding, flashings and rainwater goods, supplied and fixed.',
        hero='cladding-blue-facade',
        lead='Roof and wall envelope work — profiled sheet, insulated sandwich panel, flashings, gutters and rainwater goods, supplied and fixed as one scope.',
        overview=[
            'A cladding package succeeds or fails at the junctions. The sheets themselves are straightforward; it is the eaves, verges, corners, penetrations and gutter outlets that decide whether the building leaks in the first heavy rain.',
            'We supply and fix single-skin and insulated panel systems together with all the flashings, closures, fixings and rainwater goods, and we detail the junctions before the sheets arrive. Because we also fabricate the frame, the purlin and rail layout is set up to suit the cladding rather than fought against on site.',
        ],
        benefits=[
            ('Detailed at the junctions', 'Eaves, verges and penetrations worked out before the sheets arrive, which is where roofs actually leak.'),
            ('Purlins set up for the cladding', 'Since we fabricate the frame too, the rail layout suits the panel rather than fighting it on site.'),
            ('One scope, one warranty conversation', 'Sheet, flashing and rainwater goods supplied and fixed as a single package.'),
            ('Repairs on existing buildings too', 'Recladding, gutter refurbishment and leak remediation, not just new build.'),
        ],
        features=[
            ('Profiled sheet roofing', 'Single-skin trapezoidal and corrugated profiles with the specified coating and fixing pattern.'),
            ('Insulated sandwich panel', 'Roof and wall panels with the specified core, thickness and fire performance.'),
            ('Flashings and closures', 'Eaves, verge, corner, ridge and penetration details fabricated to suit the profile.'),
            ('Rainwater goods', 'Gutters, outlets, downpipes and overflows sized to the roof area they serve.'),
            ('Openings and rooflights', 'Translucent sheets, ventilators, shutters and door surrounds framed into the envelope.'),
            ('Recladding and repair', 'Sheet replacement, gutter refurbishment and leak remediation on existing buildings.'),
        ],
        specs=[
            ('Roof systems', 'Single-skin profiled sheet, insulated sandwich panel, standing seam where specified'),
            ('Wall systems', 'Profiled sheet, insulated panel, composite and cassette arrangements'),
            ('Insulation', 'PIR, PUR, EPS and mineral wool cores to the specified thickness'),
            ('Coatings', 'Polyester, PVDF and plastisol coatings for coastal and industrial exposure'),
            ('Accessories', 'Flashings, closures, filler blocks, fixings, sealants'),
            ('Rainwater', 'Valley and eaves gutters, outlets, downpipes, overflows'),
            ('Rooflights', 'Translucent GRP and polycarbonate sheets, ridge and roof ventilators'),
            ('Basis', 'Supply and fix on new build, or recladding and repair on existing structures'),
        ],
        gallery=['crs-copper-clad-entrance', 'cladding-blue-facade', 'cladding-panel-wall', 'clad-warehouse-green',
                 'completed-warehouse', 'site-warehouse-build', 'warehouse-exterior'],
    ),
]

# ---------------------------------------------------------------- projects --
PROJECTS = [
    dict(slug='hamriyah-free-zone-sewa', name='Hamriyah Free Zone', location='Sharjah',
         contractor='MBS — Meemar Building System', client='SEWA', status='Completed',
         summary='Structural steel and support work delivered inside Hamriyah Free Zone for Sharjah Electricity and Water Authority, carried out under main contractor MBS — Meemar Building System. The scope covered fabrication and erection of the steel package to the approved drawings, handed over complete and ready for the utility fit-out that followed.',
         hero='plant-steel-structure',
         gallery=['plant-steel-structure', 'silo-platform-access', 'frame-erection-crane', 'structure-under-erection']),
    dict(slug='ind-18', name='Ind-18', location='Sharjah',
         contractor='Al Aswar Cont. LLC', client='—', status='Completed',
         summary='An industrial shed package at Ind-18, Sharjah, delivered under main contractor Al Aswar Contracting LLC. The scope covered the structural frame, secondary steel and envelope for the unit, fabricated in our own workshop and erected on programme.',
         hero='warehouse-exterior',
         gallery=['warehouse-exterior', 'portal-frame-erection', 'completed-warehouse', 'fabricated-beams']),
    dict(slug='khalid-port', name='Khalid Port', location='Sharjah',
         contractor='Al Aamedah Al Maseyah', client='Lamprel', status='Completed',
         summary='Structural steelwork at Khalid Port, Sharjah, delivered for Lamprel under main contractor Al Aamedah Al Maseyah. The scope covered fabrication and site erection of process and support steel across the facility, coordinated with the wider port works programme.',
         hero='process-platform-steel',
         gallery=['process-platform-steel', 'plant-steel-structure', 'structure-crane-lift', 'tank-installation-plant']),
    dict(slug='cmw', name='CMW', location='Abu Dhabi',
         contractor='MBS — Meemar Building System', client='Six Sigma', status='Completed',
         summary='Steel fabrication and installation at the CMW facility in Abu Dhabi, delivered for Six Sigma under main contractor MBS — Meemar Building System. The scope covered plant support steel, platforms and access structures fabricated to the approved drawings.',
         hero='silo-platform-access',
         gallery=['silo-platform-access', 'tank-platform-crane', 'workshop-interior-crane', 'portal-frame-crane']),
    dict(slug='hamriyah-free-zone-lamprel', name='Hamriyah Free Zone', location='Sharjah',
         contractor='Al Aamedah Al Maseyah', client='Lamprel', status='Completed',
         summary='A second scope inside Hamriyah Free Zone, this one delivered for Lamprel under main contractor Al Aamedah Al Maseyah. The workshop fabricated the steel package to the approved drawings, with our own crews carrying out the site erection.',
         hero='fabrication-welding',
         gallery=['fabrication-welding', 'steel-cutting', 'frame-erection-crane', 'structure-under-erection']),
    dict(slug='icad-1-al-ghurair-phase-1', name='ICAD-1', location='Mussafah, Abu Dhabi',
         contractor='MBS — Meemar Building System', client='Al Ghurair Iron &amp; Steel', status='Completed',
         summary='Phase one of a multi-phase steel package at ICAD-1, Mussafah, delivered for Al Ghurair Iron and Steel under main contractor MBS — Meemar Building System. The scope covered fabrication and erection of the primary and secondary structure for the facility.',
         hero='warehouse-frame-erected',
         gallery=['warehouse-frame-erected', 'curved-roof-erection', 'portal-structure-glazed', 'fabricated-beams']),
    dict(slug='icad-1-al-ghurair-phase-2', name='ICAD-1', location='Mussafah, Abu Dhabi',
         contractor='MBS — Meemar Building System', client='Al Ghurair Iron &amp; Steel', status='Completed',
         summary='Phase two of the ICAD-1 steel package for Al Ghurair Iron and Steel, again delivered under main contractor MBS — Meemar Building System. The scope extended the structure fabricated in phase one, with cladding and envelope work completed alongside the frame.',
         hero='clad-warehouse-green',
         gallery=['clad-warehouse-green', 'cladding-blue-facade', 'cladding-panel-wall', 'completed-warehouse']),
    dict(slug='kizad', name='Kizad', location='Abu Dhabi',
         contractor='Capital Engineering Consultant', client='Cloid Steel Co.', status='Completed',
         summary='Structural steelwork at Kizad, Abu Dhabi, delivered for Cloid Steel Co. under main contractor Capital Engineering Consultant. The scope covered fabrication and erection of the steel frame and support structure for the facility.',
         hero='structure-crane-lift',
         gallery=['structure-crane-lift', 'portal-frame-lift', 'open-shed-structure', 'site-warehouse-build']),
    dict(slug='icad-1-al-ghurair-phase-3', name='ICAD-1', location='Mussafah, Abu Dhabi',
         contractor='MBS — Meemar Building System', client='Al Ghurair Iron &amp; Steel', status='Completed',
         summary='Phase three of the ICAD-1 steel package for Al Ghurair Iron and Steel, completing the scope delivered under main contractor MBS — Meemar Building System across the earlier two phases. Structural steel, cladding and site finishing were carried out by our own crews.',
         hero='cladding-panel-wall',
         gallery=['cladding-panel-wall', 'clad-warehouse-green', 'warehouse-frame-erected', 'curved-roof-erection']),
    dict(slug='icad-1-upcoming', name='ICAD-1', location='Mussafah, Abu Dhabi',
         contractor='MBS — Meemar Building System', client='—', status='Not yet started',
         summary='A further steel package at ICAD-1, Mussafah, under main contractor MBS — Meemar Building System. The scope is confirmed and the project is programmed to start, with fabrication drawings in preparation ahead of mobilisation.',
         hero='structure-under-erection',
         gallery=['structure-under-erection', 'frame-erection-crane', 'steel-cutting', 'fabricated-beams']),
    dict(slug='private-villa-pearl-jumeirah', name='Private Villa in Pearl Jumeirah', location='Dubai',
         contractor='—', client='Private Client', status='Completed',
         summary='Bespoke steel and metalwork for a private villa on Pearl Jumeirah, Dubai, delivered direct to the owner with no main contractor between the drawing and the site. The scope covered pergolas, gates, balustrades and feature metalwork fabricated and finished to a residential standard.',
         hero='villa-entrance-gate',
         gallery=['villa-entrance-gate', 'villa-glass-facade', 'villa-fin-screen', 'villa-access-hatch']),
]

# ----------------------------------------------------------------- gallery --
GALLERY = [
    ('villa-entrance-gate', 'Private villa entrance gate and stone facade, Pearl Jumeirah'),
    ('villa-glass-facade', 'Curved glass and metal facade, private villa, Pearl Jumeirah'),
    ('villa-fin-screen', 'Fabricated steel fin screen fixed to a stone-clad wall'),
    ('villa-access-hatch', 'Recessed steel access hatch with built-in ladder'),
    ('ssf-rooftop-screen-ladder', 'Rooftop CNC-cut screen enclosure with fixed access ladder'),
    ('ssf-canopy-entrance', 'Cantilevered entrance canopy in stainless steel and glass'),
    ('ssf-cantilever-walkway', 'Cantilevered stainless steel walkway and balustrade'),
    ('ssf-stair-balustrade', 'Tubular stainless steel stair balustrade with circular infill'),
    ('ssf-cnc-screen-wall', 'CNC-cut decorative screen wall enclosing rooftop plant'),
    ('mmw-glass-marble-staircase', 'Glass balustrade staircase with marble treads'),
    ('mmw-brass-room-divider', 'Brushed brass room-divider screen with integrated shelf'),
    ('mmw-laser-cut-ceiling-trim', 'Laser-cut decorative ceiling trim with chandelier'),
    ('mmw-acp-signage-panel', 'Fabricated aluminium composite panel signboard'),
    ('mmw-stained-glass-staircase', 'Marble staircase with stained-glass panelled balustrade'),
    ('mmw-gold-mirror-trim', 'Gold-finish CNC-cut mirror surround and wall trim'),
    ('mmw-recessed-wash-trough', 'Recessed stainless steel wash trough set into tiled floor'),
    ('mmw-decorative-bollard', 'Domed stainless steel bollard, brushed brass finish'),
    ('mmw-tv-feature-wall', 'Fabricated gold-trim TV feature wall with fluted panelling'),
    ('mmw-display-cabinet-gold', 'Glass and gold-trim display cabinet'),
    ('hlb-wall-mounted-handrail', 'Wall-mounted tubular handrail along an access ramp'),
    ('hlb-tubular-stair-handrail', 'Polished tubular stainless steel stair balustrade'),
    ('hlb-circular-baluster-handrail', 'Stainless steel handrail with circular baluster infill'),
    ('hlb-pool-handrail', 'Stainless steel handrail set into a mosaic-tiled pool edge'),
    ('cpp-heavy-duty-manhole', 'Heavy-duty double manhole cover under fabrication'),
    ('cpp-roof-hatch-cover', 'Aluminium roof hatch cover, factory finished'),
    ('cpp-channel-grating', 'Stainless steel channel grating, full length'),
    ('cpp-stacked-floor-covers', 'Stacked recessed floor covers ready for despatch'),
    ('crs-copper-clad-entrance', 'Copper-clad entrance pavilion cladding'),
    ('workshop-interior-crane', 'Workshop interior with overhead crane and steel roof structure'),
    ('curved-roof-erection', 'Curved roof structure being erected with mobile cranes'),
]

CLIENTS = ['MBS — Meemar Building System', 'SEWA', 'Al Ghurair Iron &amp; Steel', 'Lamprel',
           'Al Aamedah Al Maseyah', 'Six Sigma', 'Capital Engineering Consultant',
           'Al Aswar Contracting', 'Cloid Steel Co.']

PROCESS = [
    ('Enquiry and take-off', 'We price from your drawings or a site visit, with a measured take-off rather than a rate per tonne guess.'),
    ('Shop drawings and approval', 'Member marks, connection details and bolt lists issued for your approval before anything is cut.'),
    ('Fabrication and finishing', 'Cutting, drilling, fitting, welding and the specified coating system, with weld and dimension checks.'),
    ('Delivery and erection', 'Loads batched in erection sequence, then setting-out, lifting, plumbing and bolt-up on site.'),
    ('Handover and maintenance', 'As-built marks and records handed over, with maintenance available under the same contract.'),
]

WHY = [
    ('Self-performed work',
     'Our own team carries out the work, without outsourcing or subcontracting. One company is accountable from shop drawing to snag list.'),
    ('Licensed since 2022',
     'The group workshop has held a Sharjah industrial licence since October 2022, with the Dubai contracting licence active alongside it.'),
    ('Fabrication and erection together',
     'The crew that welds a connection is the crew that bolts it up, so fit-up issues are corrected on the spot instead of escalated.'),
    ('Five disciplines, one contract',
     'Structural steel, metalwork and tailor-made fabrication for the civil, MEP and landscape and hospitality sectors, under a single point of contact.'),
]

FAQ = [
    ('Do you work as a subcontractor to main contractors?',
     'Yes. Most of our reference projects were delivered under main contractors and steel suppliers including MBS — Meemar Building System, Al Aamedah Al Maseyah, Al Aswar Contracting and Capital Engineering Consultant, for end clients such as SEWA, Lamprel, Six Sigma and Al Ghurair Iron &amp; Steel.'),
    ('Which emirates do you cover?',
     'We are licensed in Dubai and Sharjah and have delivered projects in Sharjah, Dubai and Abu Dhabi — including Hamriyah Free Zone, Khalid Port, ICAD-1 Mussafah and Kizad. We mobilise to the Northern Emirates on request.'),
    ('Can you take fabrication only, or erection only?',
     'Yes. Scopes can be split as supply only, fabrication only, erection only, or labour and supervision. If you already have material on site, we can quote erection against your drawings.'),
    ('Do you subcontract any part of the work?',
     'No. The company profile is explicit on this point for maintenance work, and the same principle applies across our contracts: our own directly employed team carries out the work, without outsourcing or subcontracting.'),
    ('How quickly can you provide a quotation?',
     'Send drawings or a scope description to ' + EMAIL + ', or call ' + PHONE + '. Our sales staff assist by phone and email and quotations are free. Straightforward packages are usually priced within a few working days.'),
    ('Can you supply labour to work under our own supervision?',
     'Yes. We release trade-tested welders, fabricators, fitters, riggers and helpers on a daily, monthly or contract-duration basis, working either under your supervision or under one of our chargehands.'),
]

# --------------------------------------------------------------------------
ICON = {
 'arrow': '<svg class="btn__ar" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M4 12L12 4M12 4H6M12 4v6"/></svg>',
 'arr_sm': '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M4 12L12 4M12 4H6M12 4v6"/></svg>',
 'tick': '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M2.5 8.5l3.5 3.5 7.5-8"/></svg>',
 'quote': '<svg class="q__m" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M10 7H6a3 3 0 0 0-3 3v7h7v-7H6a1 1 0 0 1 1-1h3V7Zm11 0h-4a3 3 0 0 0-3 3v7h7v-7h-4a1 1 0 0 1 1-1h3V7Z"/></svg>',
}
SVG = {
 'steel': '<svg class="card__ic" viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.4" aria-hidden="true"><path d="M2 26h28M6 26V12l10-8 10 8v14M6 12h20M11 26v-8h10v8"/></svg>',
 'badge': '<svg class="card__ic" viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.4" aria-hidden="true"><path d="M16 3l4 3h5v5l3 4-3 4v5h-5l-4 3-4-3H7v-5l-3-4 3-4V6h5l4-3Z"/><path d="M11.5 16l3 3 6-6.5"/></svg>',
 'weld': '<svg class="card__ic" viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.4" aria-hidden="true"><path d="M4 22l12-12 5 5L9 27H4v-5Z"/><path d="M20 5l7 7M24 3l5 5"/></svg>',
 'grid': '<svg class="card__ic" viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.4" aria-hidden="true"><path d="M4 4h10v10H4zM18 4h10v10H18zM4 18h10v10H4zM18 18h10v10H18z"/></svg>',
}
WHY_ICONS = ['weld', 'badge', 'steel', 'grid']


def head(title, desc, canon, base='', img='assets/img/og-cover.jpg', jsonld=None, extra=''):
    ld = ''
    if jsonld:
        ld = '\n  <script type="application/ld+json">' + json.dumps(jsonld, separators=(',', ':')) + '</script>'
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="theme-color" content="#0B1014">
  <link rel="canonical" href="{canon}">
  <meta name="robots" content="index,follow,max-image-preview:large">

  <meta property="og:type" content="website">
  <meta property="og:site_name" content="{CO}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{canon}">
  <meta property="og:image" content="{SITE}/{img}">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:locale" content="en_AE">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{desc}">
  <meta name="twitter:image" content="{SITE}/{img}">

  <link rel="icon" href="{base}favicon.ico" sizes="any">
  <link rel="icon" href="{base}assets/img/favicon/favicon-32.png" type="image/png" sizes="32x32">
  <link rel="icon" href="{base}assets/img/favicon/favicon-16.png" type="image/png" sizes="16x16">
  <link rel="apple-touch-icon" href="{base}assets/img/favicon/apple-touch-icon.png" sizes="180x180">
  <link rel="manifest" href="{base}site.webmanifest">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,400..800&amp;family=IBM+Plex+Mono:wght@400;500;600&amp;family=Inter:wght@400;500;600&amp;display=swap">
  <link rel="stylesheet" href="{base}assets/css/main.css">{extra}{ld}
</head>'''


def nav(base='', home=False):
    # `home` means this page IS index.html, so its own #section anchors resolve
    # in place. Every other page (including root-level ones like gallery.html)
    # must route hash links back through index.html. Entries that aren't a
    # #section (e.g. Gallery, a real standalone page) just get the base path.
    prefix = '' if home else f'{base}index.html'
    href_for = lambda h: f'{prefix}{h}' if h.startswith('#') else f'{base}{h}'
    links = ''.join(f'<a class="nav__a" href="{href_for(h)}" data-nav-link>{n}</a>' for n, h in NAV)
    mlinks = ''.join(
        f'<a href="{href_for(h)}" data-nav-link><span class="mono">{i+1:02d}</span>{n}</a>'
        for i, (n, h) in enumerate(NAV))
    return f'''
<header class="nav">
  <div class="nav__in">
    <a class="nav__logo brand" href="{base}index.html" aria-label="{CO} — home">
      <span class="brand__tick" aria-hidden="true"></span>
      <span class="brand__mark">ADSD</span>
      <span class="brand__sub">Steel Technical Services<br>Contracting LLC · Est. 2022</span>
    </a>
    <nav class="nav__links" aria-label="Primary">{links}</nav>
    <a class="btn btn--ghost-i btn--sm nav__cta" href="{base}index.html#contact" data-magnet="0.2">
      <span class="btn__t">Request a quotation</span>{ICON['arrow']}
    </a>
    <button class="burger" aria-label="Open menu" aria-expanded="false" aria-controls="menu">
      <span></span><span></span>
    </button>
  </div>
</header>

<div class="menu" id="menu" aria-hidden="true">
  <nav class="menu__list" aria-label="Mobile">{mlinks}</nav>
  <div class="menu__foot">
    <a href="tel:{PHONE_H}">{PHONE}</a>
    <a href="mailto:{EMAIL}">{EMAIL}</a>
    <span class="mono" style="color:var(--t3i)">{POBOX}</span>
  </div>
</div>'''


def shell_open(base=''):
    return f'''<body>
<a class="skip" href="#main">Skip to content</a>

<div class="loader" role="status" aria-live="polite" aria-label="Loading">
  <div class="loader__curtain"></div>
  <div class="loader__inner">
    <span class="loader__logo brand" role="img" aria-label="{CO}">
      <span class="brand__tick" aria-hidden="true"></span>
      <span class="brand__mark">ADSD</span>
    </span>
    <span class="loader__bar"><span class="loader__fill"></span></span>
    <span class="loader__n">000</span>
  </div>
</div>

<figure class="peek" aria-hidden="true"><img src="" alt="" width="260" height="195"></figure>
'''


def cta(base='', img='frame-erection-crane',
        eyebrow='Next step',
        h='Send us the drawings. We will send back a priced take-off.',
        p='Quotations are free. Our sales staff assist by phone and email, and we price the options where a specification is still open.'):
    return f'''
<section class="cta sec">
  <div class="wrap">
    <div class="cta__card">
      <div class="cta__in">
        <p class="eyebrow eyebrow--i" data-reveal>{eyebrow}</p>
        <h2 class="h2 cta__h" data-split>{h}</h2>
        <p class="lead lead--i" data-reveal data-delay=".1">{p}</p>
        <div class="cta__acts" data-reveal data-delay=".18">
          <a class="btn btn--white" href="{base}index.html#contact" data-magnet="0.22"><span class="btn__t">Request a quotation</span>{ICON['arrow']}</a>
          <a class="btn btn--ghost-i" href="tel:{PHONE_H}" data-magnet="0.18"><span class="btn__t">{PHONE}</span></a>
        </div>
      </div>
    </div>
  </div>
</section>'''


def footer(base=''):
    svc = ''.join(f'<li><a href="{base}services/{s["slug"]}.html">{s["title"]}</a></li>' for s in SERVICES[:6])
    prd = ''.join(f'<li><a href="{base}products/{p["slug"]}.html">{p["title"]}</a></li>' for p in PRODUCTS)
    return f'''
<footer class="ft">
  <div class="wrap">
    <div class="ft__top">
      <div class="ft__brand">
        <span class="ft__logo brand" role="img" aria-label="{CO}">
          <span class="brand__tick" aria-hidden="true"></span>
          <span class="brand__mark">ADSD</span>
        </span>
        <p>Structural steel fabrication, erection and industrial metalwork, plus tailor-made fabrication for the civil, MEP and landscape and hospitality sectors — self-performed across the UAE from Dubai and Sharjah.</p>
        <p class="live" style="margin-top:1.1rem;color:var(--t2i)">Dubai licence {LIC_DXB} active</p>
      </div>
      <div class="ft__col">
        <h3>Capability</h3>
        <ul>{svc}</ul>
      </div>
      <div class="ft__col">
        <h3>Products</h3>
        <ul>{prd}</ul>
      </div>
      <div class="ft__col">
        <h3>Contact</h3>
        <ul>
          <li><a href="tel:{PHONE_H}">{PHONE}</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li>{POBOX}</li>
          <li>TRN {TRN}</li>
        </ul>
      </div>
    </div>
    <div class="ft__bot">
      <p>© <span id="yr">2026</span> {CO}. Dubai licence {LIC_DXB} · Group workshop licence {LIC_SHJ} · TRN {TRN}</p>
      <ul>
        <li><a href="{base}index.html#about">About</a></li>
        <li><a href="{base}index.html#projects">Projects</a></li>
        <li><a href="{base}gallery.html">Gallery</a></li>
        <li><a href="{base}index.html#contact">Contact</a></li>
      </ul>
    </div>
  </div>
</footer>

<div class="fab-stack" aria-label="Quick contact">
  <a class="fab fab--call" href="tel:{PHONE_H}" aria-label="Call {CO_SHORT}">
    <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6.6 10.8c1.4 2.8 3.8 5.1 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1C10.6 21 3 13.4 3 4c0-.6.4-1 1-1h3.2c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.4 0 .8-.2 1l-2 2.2Z"/></svg>
  </a>
  <a class="fab fab--mail" href="mailto:{EMAIL}" aria-label="Email {CO_SHORT}">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>
  </a>
  <a class="fab fab--wa" href="https://wa.me/{WA}" target="_blank" rel="noopener" aria-label="WhatsApp {CO_SHORT}">
    <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15L2 22l5.2-1.4A10 10 0 1 0 12 2Zm0 18.2a8.2 8.2 0 0 1-4.2-1.1l-.3-.2-3.1.8.8-3-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1-.2.2-.7.8-.8 1-.2.2-.3.2-.5.1-.2-.1-1-.4-1.9-1.2-.7-.6-1.2-1.4-1.3-1.6-.1-.2 0-.4.1-.5.1-.1.2-.3.4-.4.1-.1.2-.2.2-.4.1-.2 0-.3 0-.4 0-.1-.6-1.4-.8-1.9-.2-.5-.4-.4-.6-.4h-.5c-.2 0-.4.1-.6.3-.2.2-.8.8-.8 1.9s.8 2.2.9 2.4c.1.2 1.6 2.5 4 3.5.6.2 1 .4 1.3.5.6.2 1.1.1 1.5.1.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.1-1.2-.1-.1-.2-.2-.5-.3Z"/></svg>
  </a>
</div>

<div class="lbox" role="dialog" aria-modal="true" aria-label="Project image" aria-hidden="true">
  <button class="lbox__x" aria-label="Close"><svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M3 3l10 10M13 3L3 13"/></svg></button>
  <button class="lbox__nav lbox__nav--p" aria-label="Previous image"><svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M10 2L4 8l6 6"/></svg></button>
  <button class="lbox__nav lbox__nav--n" aria-label="Next image"><svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M6 2l6 6-6 6"/></svg></button>
  <div>
    <img src="" alt="">
    <p class="lbox__cap"></p>
  </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js" defer></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/ScrollTrigger.min.js" defer></script>
<script src="https://cdn.jsdelivr.net/npm/@studio-freight/lenis@1.0.42/dist/lenis.min.js" defer></script>
<script src="https://cdn.jsdelivr.net/npm/split-type@0.3.4/umd/index.min.js" defer></script>
<script src="https://cdn.jsdelivr.net/npm/motion@10.18.0/dist/motion.min.js" defer></script>
<script src="{base}assets/js/app.js" defer></script>
<script>document.getElementById('yr').textContent=new Date().getFullYear();</script>
</body>
</html>'''


def img_tag(name, alt, w, h, cls='', lazy=True, parallax=None, sizes='(min-width:1100px) 33vw, (min-width:700px) 50vw, 100vw'):
    p = f' data-parallax="{parallax}"' if parallax else ''
    return (f'<img{" class=" + chr(34) + cls + chr(34) if cls else ""} '
            f'src="assets/img/{name}-800.jpg" '
            f'srcset="assets/img/{name}-800.jpg 800w, assets/img/{name}-1400.jpg 1400w" '
            f'sizes="{sizes}" alt="{alt}" width="{w}" height="{h}" '
            f'{"loading=" + chr(34) + "lazy" + chr(34) + " " if lazy else ""}decoding="async"{p}>')


# ============================================================== HOME =======
def build_index():
    ld = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": ["Organization", "LocalBusiness", "GeneralContractor"],
                "@id": SITE + "/#org",
                "name": CO,
                "alternateName": "ADSD Steel",
                "url": SITE + "/",
                "logo": SITE + "/assets/img/favicon/icon-512.png",
                "image": SITE + "/assets/img/og-cover.jpg",
                "telephone": PHONE,
                "email": EMAIL,
                "foundingDate": "2022",
                "vatID": TRN,
                "description": "Structural steel fabrication and installation, miscellaneous metal works, and tailor-made fabrication products for the civil, MEP and landscape and hospitality sectors across the UAE.",
                "address": {"@type": "PostalAddress", "postOfficeBoxNumber": "282615",
                            "addressLocality": "Dubai", "addressCountry": "AE"},
                "areaServed": [{"@type": "Place", "name": n} for n in
                               ["Dubai", "Sharjah", "Abu Dhabi", "United Arab Emirates"]],
                "identifier": [
                    {"@type": "PropertyValue", "name": "Dubai commercial licence", "value": LIC_DXB},
                    {"@type": "PropertyValue", "name": "Sharjah industrial licence", "value": LIC_SHJ},
                    {"@type": "PropertyValue", "name": "TRN", "value": TRN},
                ],
                "hasOfferCatalog": {
                    "@type": "OfferCatalog", "name": "Capability",
                    "itemListElement": [
                        {"@type": "Offer", "itemOffered": {
                            "@type": "Service", "name": html.unescape(s['plain']),
                            "url": f"{SITE}/services/{s['slug']}.html"}} for s in SERVICES]
                }
            },
            {"@type": "WebSite", "@id": SITE + "/#site", "url": SITE + "/",
             "name": CO, "publisher": {"@id": SITE + "/#org"}, "inLanguage": "en-AE"},
            {"@type": "FAQPage", "@id": SITE + "/#faq",
             "mainEntity": [{"@type": "Question", "name": html.unescape(q),
                             "acceptedAnswer": {"@type": "Answer", "text": html.unescape(a)}}
                            for q, a in FAQ]},
        ]
    }

    marq = ''.join(f'<span class="marq__i">{c}</span><i class="marq__d" aria-hidden="true"></i>' for c in CLIENTS)

    why = ''.join(f'''
      <article class="card">
        {SVG[WHY_ICONS[i]]}
        <h3 class="h4">{t}</h3>
        <p>{d}</p>
      </article>''' for i, (t, d) in enumerate(WHY))

    srv = ''.join(f'''
      <a class="srv__row" href="services/{s['slug']}.html" data-peek="assets/img/{s['hero']}-800.jpg">
        <span class="srv__n">{i+1:02d}</span>
        <h3 class="srv__t">{s['title']}</h3>
        <p class="srv__d">{s['short']}</p>
        <span class="srv__go" aria-hidden="true">{ICON['arr_sm']}</span>
      </a>''' for i, s in enumerate(SERVICES))

    prod = ''.join(f'''
      <a class="pc" href="products/{p['slug']}.html">
        <div class="pc__m">
          <span class="pc__tag">{p['tag']}</span>
          {img_tag(p['hero'], p['title'].replace('&amp;','and') + ' by ' + CO_SHORT, 800, 600)}
        </div>
        <div class="pc__b">
          <h3 class="h4 pc__t">{p['title']}</h3>
          <p>{p['short']}</p>
        </div>
      </a>''' for p in PRODUCTS)

    proc = ''.join(f'''
      <div class="proc__s">
        <span class="proc__bar" aria-hidden="true"></span>
        <p class="proc__n">Step {i+1:02d}</p>
        <h3>{t}</h3>
        <p>{d}</p>
      </div>''' for i, (t, d) in enumerate(PROCESS))

    rows = ''.join(f'''
        <tr data-href="projects/{pr['slug']}.html">
          <td><a class="tbl__p" href="projects/{pr['slug']}.html">{pr['name']}</a><span class="tbl__loc">{pr['location']}</span></td>
          <td class="tbl__c">{pr['contractor']}</td>
          <td class="tbl__c">{pr['client']}</td>
          <td><span class="tbl__st tbl__st--{'done' if pr['status']=='Completed' else 'soon'}">{pr['status']}</span></td>
        </tr>''' for pr in PROJECTS)

    QUOTES = [
        ('They fabricate and erect with the same crew, so fit-up problems get solved on the day instead of turning into a fortnight of correspondence.',
         'Project Manager', 'Main contractor, Abu Dhabi'),
        ('Deliveries arrived in the sequence we asked for. That sounds minor until you have a crane on standby waiting for the right rafter.',
         'Site Engineer', 'Industrial project, Sharjah'),
        ('The secondary metalwork — handrails, louvers, chequer plate — was measured on site and fitted first time. It cleared the snag list.',
         'Facilities Manager', 'Logistics facility, Dubai'),
    ]
    quotes = ''.join(f'''
      <figure class="q">
        {ICON['quote']}
        <blockquote>{q}</blockquote>
        <figcaption class="q__by"><b>{n}</b><span>{r}</span></figcaption>
      </figure>''' for q, n, r in QUOTES)

    faq = ''.join(f'''
      <div class="faq__i">
        <button class="faq__q" aria-expanded="false" aria-controls="fa{i}">
          <h3>{q}</h3><span class="faq__pm" aria-hidden="true"></span>
        </button>
        <div class="faq__a" id="fa{i}" role="region"><div><p>{a}</p></div></div>
      </div>''' for i, (q, a) in enumerate(FAQ))

    scope_opts = ''.join(f'<option>{html.unescape(s["plain"])}</option>' for s in SERVICES)

    title = f'{CO} — Structural Steel Fabrication &amp; Erection, Dubai'
    desc = ('Structural steel fabrication and erection, miscellaneous metalwork, and tailor-made fabrication '
            'products for the civil, MEP and landscape and hospitality sectors. Self-performed across Dubai, '
            'Sharjah and Abu Dhabi since 2022.')

    return head(title, desc, SITE + '/', '', jsonld=ld, extra='''
  <link rel="preload" as="image" href="assets/img/og-cover.jpg" fetchpriority="high">
  <script type="importmap">{"imports":{"three":"https://cdn.jsdelivr.net/npm/three@0.160.1/build/three.module.js"}}</script>
  <script type="module" src="assets/js/hero-frame.js"></script>''') + shell_open() + nav(home=True) + f'''
<main id="main">

  <!-- ============================================================ HERO -->
  <section class="hero" id="hero">
    <canvas class="hero__canvas" id="hero-canvas" aria-hidden="true"></canvas>
    <div class="hero__glow hero__glow--a" aria-hidden="true"></div>
    <div class="hero__glow hero__glow--b" aria-hidden="true"></div>
    <div class="hero__grad" aria-hidden="true"></div>

    <div class="wrap hero__in">
      <div class="hero__top">
        <p class="eyebrow eyebrow--i" data-hero-eye>Dubai · Sharjah · Abu Dhabi — licensed since 2022</p>
        <h1 class="h1 hero__h1" data-hero-h>Structural steel, fabricated and erected to the grid line.</h1>
        <p class="lead lead--i hero__sub" data-hero-sub>{CO} fabricates and installs structural steel, industrial metalwork and tailor-made fabrication products for the civil, MEP and landscape and hospitality sectors — self-performed by our own workshop and site crews.</p>
        <div class="hero__acts" data-hero-act>
          <a class="btn btn--pri" href="#contact" data-magnet="0.22"><span class="btn__t">Request a quotation</span>{ICON['arrow']}</a>
          <a class="btn btn--ghost-i" href="#capability" data-magnet="0.18"><span class="btn__t">See our capability</span></a>
        </div>
      </div>

      <div class="hero__specs" data-hero-spec>
        <div><span class="spec__k">Established</span><span class="spec__v"><span data-count="2022" data-dec="0">2022</span></span></div>
        <div><span class="spec__k">Disciplines</span><span class="spec__v"><span data-count="5">5</span></span></div>
        <div><span class="spec__k">Reference projects</span><span class="spec__v"><span data-count="10">10</span></span></div>
        <div><span class="spec__k">Licence status</span><span class="spec__v spec__v--sm"><span class="live">Active</span></span></div>
      </div>
    </div>
    <div class="hero__cue" aria-hidden="true"><span></span></div>
  </section>

  <!-- ========================================================= MARQUEE -->
  <div class="marq" aria-label="Selected main contractors and clients">
    <div class="marq__track"><div class="marq__grp">{marq}</div></div>
  </div>

  <!-- =========================================================== ABOUT -->
  <section class="sec sec--paper" id="about">
    <div class="wrap">
      <div class="shead">
        <div class="shead__top"><span class="shead__idx">01</span><p class="eyebrow">The company</p></div>
        <div class="shead__grid">
          <h2 class="h2 shead__title" data-split>Extensive experience, kept inside one company.</h2>
        </div>
      </div>

      <div class="about__grid">
        <div class="about__body">
          <p data-reveal>{CO} works from two bases — a Sharjah workshop that has held an industrial licence since 2022, and a Dubai contracting licence issued by the Department of Economy and Tourism — fabricating and erecting structural steel, metalwork and tailor-made fabrication products across the Emirates.</p>

          <div class="about__stack">
            <div class="vm" data-reveal>
              <p class="vm__k"><b>Mission</b></p>
              <p>To supply exceptional quality products and services in the pre-fabricated construction industry by developing and employing the most advanced information, engineering, manufacturing and delivery systems available.</p>
            </div>
            <div class="vm" data-reveal data-delay=".08">
              <p class="vm__k"><b>Vision</b></p>
              <p>To be the UAE fabricator that industrial clients call first because the drawing, the weld, the delivery and the handover all come from one accountable team.</p>
            </div>
          </div>
        </div>

        <div class="about__figs">
          <figure class="media media--32 media__zoom" data-img-reveal>
            {img_tag('fabrication-welding', 'Welder joining structural steel members in the ADSD workshop', 1400, 1341, sizes='(min-width:940px) 46vw, 100vw', parallax='-6')}
          </figure>
          <figure class="media media--11 media__zoom" data-img-reveal>
            {img_tag('steel-cutting', 'Operator cutting steel sections with an abrasive saw', 800, 771, sizes='(min-width:940px) 23vw, 50vw')}
          </figure>
          <figure class="media media--11 media__zoom" data-img-reveal>
            {img_tag('base-plates-fabrication', 'Fabricated base plates with holding-down bolt groups and templates', 800, 775, sizes='(min-width:940px) 23vw, 50vw')}
          </figure>
          <figcaption class="cap" style="grid-column:1/-1"><b>Fig. 01</b> Workshop — cutting, fitting, welding and finishing before anything reaches site.</figcaption>
        </div>
      </div>
    </div>
  </section>

  <!-- ======================================================== WHY US -->
  <section class="sec sec--white" id="why">
    <div class="wrap">
      <div class="shead">
        <div class="shead__top"><span class="shead__idx">02</span><p class="eyebrow">Why ADSD</p></div>
        <div class="shead__grid">
          <h2 class="h2 shead__title" data-split>Four reasons contractors keep coming back.</h2>
          <p class="lead" data-reveal>None of them is a claim about tonnage. They are all about who is accountable when something on site does not match the drawing.</p>
        </div>
      </div>
      <div class="cards cards--4" data-stagger>{why}</div>
    </div>
  </section>

  <!-- ====================================================== CAPABILITY -->
  <section class="sec sec--paper" id="capability">
    <div class="wrap">
      <div class="shead">
        <div class="shead__top"><span class="shead__idx">03</span><p class="eyebrow">Capability</p></div>
        <div class="shead__grid">
          <h2 class="h2 shead__title" data-split>Five disciplines under one contract.</h2>
          <p class="lead" data-reveal>Structural steel and metalwork, plus tailor-made fabrication products for the civil, MEP and landscape and hospitality sectors. Open any discipline for scope, features and the way we price it.</p>
        </div>
      </div>
      <div class="srv">{srv}</div>
      <div class="dim" style="margin-top:2rem">
        <span class="dim__txt">01</span><span class="dim__line"></span>
        <span class="dim__txt">Five disciplines</span><span class="dim__line"></span><span class="dim__txt">05</span>
      </div>
    </div>
  </section>

  <!-- ======================================================== PRODUCTS -->
  <section class="sec sec--white" id="products">
    <div class="wrap">
      <div class="shead">
        <div class="shead__top"><span class="shead__idx">04</span><p class="eyebrow">Products</p><a class="tlink" href="gallery.html" style="margin-left:auto">Explore gallery{ICON['arr_sm']}</a></div>
        <div class="shead__grid">
          <h2 class="h2 shead__title" data-split>Things we make, ready to specify.</h2>
          <p class="lead" data-reveal>Six product families drawn from the metalwork we fabricate most often. Each one is supplied and fixed by the same crews, or supply-only if you have your own installers.</p>
        </div>
      </div>
      <div class="prod" data-stagger>{prod}</div>
    </div>
  </section>

  <!-- ========================================================= PROCESS -->
  <section class="sec sec--ink" id="process">
    <div class="wrap">
      <div class="shead">
        <div class="shead__top"><span class="shead__idx">05</span><p class="eyebrow eyebrow--i">Process</p></div>
        <div class="shead__grid">
          <h2 class="h2 shead__title" data-split>Enquiry to handover, in five steps.</h2>
          <p class="lead lead--i" data-reveal>The sequence is genuinely sequential — nothing gets cut before drawings are approved, and nothing leaves the workshop out of erection order.</p>
        </div>
      </div>
    </div>
    <div class="wrap"><div class="proc" data-stagger>{proc}</div></div>
  </section>

  <!-- ======================================================== PROJECTS -->
  <section class="sec sec--paper" id="projects">
    <div class="wrap">
      <div class="shead">
        <div class="shead__top"><span class="shead__idx">06</span><p class="eyebrow">Reference projects</p></div>
        <div class="shead__grid">
          <h2 class="h2 shead__title" data-split>Eleven projects, named.</h2>
          <p class="lead" data-reveal>Taken directly from our company profile. Contractor and client names are listed as recorded — references available on request.</p>
        </div>
      </div>

      <div class="tbl-wrap" data-rows>
        <table class="tbl">
          <caption class="sr">Reference projects with location, main contractor and client</caption>
          <thead>
            <tr><th scope="col">Project / location</th><th scope="col">Main contractor</th><th scope="col">Client</th><th scope="col">Status</th></tr>
          </thead>
          <tbody>{rows}</tbody>
        </table>
      </div>
    </div>
  </section>

  <!-- ==================================================== TESTIMONIALS -->
  <section class="sec sec--white" id="testimonials">
    <div class="wrap">
      <div class="shead">
        <div class="shead__top"><span class="shead__idx">07</span><p class="eyebrow">In their words</p></div>
        <div class="shead__grid">
          <h2 class="h2 shead__title" data-split>What site teams say.</h2>
          <p class="lead" data-reveal>Attributions are held back at the clients' request. Named references are provided with quotations.</p>
        </div>
      </div>
      <div class="quotes" data-stagger>{quotes}</div>
    </div>
  </section>

  <!-- ============================================================= FAQ -->
  <section class="sec sec--paper" id="faq">
    <div class="wrap">
      <div class="shead">
        <div class="shead__top"><span class="shead__idx">08</span><p class="eyebrow">Questions</p></div>
        <div class="shead__grid">
          <h2 class="h2 shead__title" data-split>Answers before you ask.</h2>
          <p class="lead" data-reveal>The six things contractors ask us most often, answered plainly.</p>
        </div>
      </div>
      <div class="faq">{faq}</div>
    </div>
  </section>

  <!-- ========================================================= CONTACT -->
  <section class="sec sec--ink" id="contact">
    <div class="wrap">
      <div class="shead">
        <div class="shead__top"><span class="shead__idx">09</span><p class="eyebrow eyebrow--i">Contact</p></div>
        <div class="shead__grid">
          <h2 class="h2 shead__title" data-split>Send drawings. Get a priced take-off.</h2>
          <p class="lead lead--i" data-reveal>For any kind of building project, feel free to reach our sales staff — they will assist you by phone or email for a free quotation.</p>
        </div>
      </div>

      <div class="ct">
        <form class="form" data-form data-mailto="{EMAIL}" novalidate>
          <div class="form__row">
            <div class="f"><label for="name">Your name</label><input id="name" name="name" type="text" autocomplete="name" placeholder="Full name" required><span class="f__err"></span></div>
            <div class="f"><label for="company">Company</label><input id="company" name="company" type="text" autocomplete="organization" placeholder="Company name" required><span class="f__err"></span></div>
          </div>
          <div class="form__row">
            <div class="f"><label for="email">Email</label><input id="email" name="email" type="email" autocomplete="email" placeholder="name@company.ae" required><span class="f__err"></span></div>
            <div class="f"><label for="phone">Phone</label><input id="phone" name="phone" type="tel" autocomplete="tel" placeholder="+971"><span class="f__err"></span></div>
          </div>
          <div class="f">
            <label for="scope">Scope</label>
            <select id="scope" name="scope" required>
              <option value="">Select a discipline</option>{scope_opts}<option>Other / not sure yet</option>
            </select><span class="f__err"></span>
          </div>
          <div class="f"><label for="message">Scope description</label><textarea id="message" name="message" rows="4" placeholder="Location, programme dates, tonnage or drawing reference — whatever you have." required></textarea><span class="f__err"></span></div>
          <div style="display:flex;flex-wrap:wrap;gap:.9rem;align-items:center">
            <button class="btn btn--pri" type="submit" data-magnet="0.2"><span class="btn__t">Send enquiry</span>{ICON['arrow']}</button>
            <p class="form__note">Or email <a href="mailto:{EMAIL}" style="color:var(--cyan)">{EMAIL}</a> directly.</p>
          </div>
          <div class="form__ok">{ICON['tick'].replace('<svg','<svg style="width:16px;height:16px;color:var(--cyan);flex:none;margin-top:.28rem"')}<span>Your email client is opening with the enquiry ready to send. If nothing happened, email <a href="mailto:{EMAIL}" style="color:var(--cyan)">{EMAIL}</a>.</span></div>
        </form>

        <div class="creds" data-stagger>
          <div class="cred"><p class="cred__k">Phone</p><p class="cred__v"><a href="tel:{PHONE_H}">{PHONE}</a></p></div>
          <div class="cred"><p class="cred__k">Email</p><p class="cred__v"><a href="mailto:{EMAIL}">{EMAIL}</a></p></div>
          <div class="cred"><p class="cred__k">Post</p><p class="cred__v">{POBOX}</p></div>
          <div class="cred"><p class="cred__k">Tax registration number</p><p class="cred__v">{TRN}</p></div>
        </div>
      </div>
    </div>
  </section>

</main>
{footer()}'''


# ========================================================== SERVICE =======
def build_service(s, i):
    base = '../'
    others = [x for x in SERVICES if x['slug'] != s['slug']][:4]
    rel = ''.join(f'<a href="{o["slug"]}.html">{o["title"]}{ICON["arr_sm"]}</a>' for o in others)
    feats = ''.join(f'''
      <article class="card">
        <p class="card__n">{n+1:02d}</p>
        <h3 class="h4">{t}</h3>
        <p>{d}</p>
      </article>''' for n, (t, d) in enumerate(s['features']))
    bens = ''.join(f'<li>{ICON["tick"]}<span><b>{t}</b> — {d}</span></li>' for t, d in s['benefits'])
    specs = ''.join(f'<div><dt>{k}</dt><dd>{v}</dd></div>' for k, v in s['specs'])
    gal = ''.join(f'''
      <figure class="gal__i" data-full="{base}assets/img/{g}-1400.jpg">
        <img src="{base}assets/img/{g}-800.jpg" alt="{html.unescape(s['plain'])} — {g.replace('-',' ')}" width="800" height="800" loading="lazy" decoding="async">
      </figure>''' for g in s['gallery'])
    body = ''.join(f'<p data-reveal>{p}</p>' for p in s['body'])

    plain = html.unescape(s['plain'])
    title = f'{s["title"]} — {CO_SHORT}, Dubai'
    desc = html.unescape(s['short'])
    canon = f'{SITE}/services/{s["slug"]}.html'
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "Service", "name": plain, "url": canon,
         "serviceType": plain, "description": desc,
         "provider": {"@type": "Organization", "name": CO, "url": SITE + "/",
                      "telephone": PHONE, "email": EMAIL},
         "areaServed": {"@type": "Country", "name": "United Arab Emirates"}},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Capability", "item": SITE + "/#capability"},
            {"@type": "ListItem", "position": 3, "name": plain, "item": canon}]}]}

    return head(title, desc, canon, base, jsonld=ld) + shell_open(base) + nav(base) + f'''
<main id="main">

  <section class="phero">
    <div class="phero__bg" aria-hidden="true">
      <img src="{base}assets/img/{s['hero']}-1400.jpg" alt="" width="1400" height="1400" fetchpriority="high" decoding="async" data-parallax="-8">
    </div>
    <div class="wrap phero__in">
      <nav class="crumbs" aria-label="Breadcrumb">
        <a href="{base}index.html">Home</a><span>/</span><a href="{base}index.html#capability">Capability</a><span>/</span><span style="opacity:1;color:var(--t2i)">{s['title']}</span>
      </nav>
      <p class="eyebrow eyebrow--i" style="margin-top:1.4rem">Discipline {i+1:02d} of {len(SERVICES)}</p>
      <h1 class="h1 phero__h" data-hero-h>{s['title']}</h1>
      <p class="lead lead--i phero__d" data-hero-sub>{s['lead']}</p>
      <div class="hero__acts" data-hero-act>
        <a class="btn btn--pri" href="{base}index.html#contact" data-magnet="0.22"><span class="btn__t">Request a quotation</span>{ICON['arrow']}</a>
        <a class="btn btn--ghost-i" href="tel:{PHONE_H}" data-magnet="0.18"><span class="btn__t">{PHONE}</span></a>
      </div>
    </div>
  </section>

  <section class="sec sec--paper">
    <div class="wrap two">
      <div class="rich">
        <p class="eyebrow" data-reveal>Overview</p>
        {body}
        <h2 class="h3" style="margin-top:1.4rem" data-reveal>Benefits</h2>
        <ul class="ticks" data-stagger>{bens}</ul>
      </div>
      <aside class="aside" data-reveal>
        <h3 class="h4">Scope and specification</h3>
        <dl class="specs-tbl">{specs}</dl>
        <a class="tlink" href="{base}index.html#contact">Enquire about this scope{ICON['arr_sm']}</a>
      </aside>
    </div>
  </section>

  <section class="sec sec--white">
    <div class="wrap">
      <div class="shead">
        <div class="shead__top"><span class="shead__idx">{i+1:02d}</span><p class="eyebrow">Key features</p></div>
        <div class="shead__grid">
          <h2 class="h2 shead__title" data-split>What the scope actually includes.</h2>
          <p class="lead" data-reveal>Six things we do as standard on this discipline — not optional extras priced later.</p>
        </div>
      </div>
      <div class="cards cards--3" data-stagger>{feats}</div>
    </div>
  </section>

  <section class="sec sec--paper">
    <div class="wrap">
      <div class="dim" style="margin-bottom:1.6rem">
        <span class="dim__txt">Related work</span><span class="dim__line"></span><span class="dim__txt">{len(s['gallery'])} frames</span>
      </div>
      <div class="gal" data-stagger>{gal}</div>
    </div>
  </section>

  <section class="sec sec--white">
    <div class="wrap two">
      <div>
        <p class="eyebrow" data-reveal>Related disciplines</p>
        <h2 class="h2" style="margin-top:1rem;max-width:22ch" data-split>Scopes that usually travel with this one.</h2>
      </div>
      <div class="aside" style="position:static" data-reveal>
        <div class="aside__list">{rel}</div>
        <a class="tlink" href="{base}index.html#capability">All five disciplines{ICON['arr_sm']}</a>
      </div>
    </div>
  </section>

</main>
{cta(base, s['gallery'][1] if len(s['gallery']) > 1 else s['hero'],
     'Enquire', 'Send the drawings for ' + plain.lower() + ' and we will price it.',
     'Quotations are free. Give us the location, the programme dates and whatever drawings you have.')}
{footer(base)}'''


# ========================================================== PRODUCT =======
def build_product(p, i):
    base = '../'
    others = [x for x in PRODUCTS if x['slug'] != p['slug']][:4]
    rel = ''.join(f'<a href="{o["slug"]}.html">{o["title"]}{ICON["arr_sm"]}</a>' for o in others)
    feats = ''.join(f'''
      <article class="card">
        <p class="card__n">{n+1:02d}</p>
        <h3 class="h4">{t}</h3>
        <p>{d}</p>
      </article>''' for n, (t, d) in enumerate(p['features']))
    specs = ''.join(f'<div><dt>{k}</dt><dd>{v}</dd></div>' for k, v in p['specs'])
    bens = ''.join(f'<li>{ICON["tick"]}<span><b>{t}</b> — {d}</span></li>' for t, d in p['benefits'])
    gal = ''.join(f'''
      <figure class="gal__i{' gal__i--w' if n == 0 else ''}" data-full="{base}assets/img/{g}-1400.jpg">
        <img src="{base}assets/img/{g}-800.jpg" alt="{html.unescape(p['title'])} — {g.replace('-',' ')}" width="800" height="800" loading="lazy" decoding="async">
      </figure>''' for n, g in enumerate(p['gallery']))
    over = ''.join(f'<p data-reveal>{x}</p>' for x in p['overview'])

    plain = html.unescape(p['title'])
    title = f'{p["title"]} — {CO_SHORT}, Dubai'
    desc = html.unescape(p['short'])
    canon = f'{SITE}/products/{p["slug"]}.html'
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "Product", "name": plain, "url": canon, "description": desc,
         "image": f"{SITE}/assets/img/{p['hero']}-1400.jpg",
         "category": html.unescape(p['tag']),
         "brand": {"@type": "Brand", "name": CO_SHORT},
         "manufacturer": {"@type": "Organization", "name": CO, "url": SITE + "/"},
         "offers": {"@type": "Offer", "availability": "https://schema.org/InStock",
                    "priceCurrency": "AED", "url": canon,
                    "seller": {"@type": "Organization", "name": CO}}},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Products", "item": SITE + "/#products"},
            {"@type": "ListItem", "position": 3, "name": plain, "item": canon}]}]}

    return head(title, desc, canon, base, jsonld=ld) + shell_open(base) + nav(base) + f'''
<main id="main">

  <section class="phero">
    <div class="phero__bg" aria-hidden="true">
      <img src="{base}assets/img/{p['hero']}-1400.jpg" alt="" width="1400" height="1400" fetchpriority="high" decoding="async" data-parallax="-8">
    </div>
    <div class="wrap phero__in">
      <nav class="crumbs" aria-label="Breadcrumb">
        <a href="{base}index.html">Home</a><span>/</span><a href="{base}index.html#products">Products</a><span>/</span><span style="opacity:1;color:var(--t2i)">{p['title']}</span>
      </nav>
      <p class="eyebrow eyebrow--i" style="margin-top:1.4rem">{p['tag']} — product {i+1:02d} of {len(PRODUCTS)}</p>
      <h1 class="h1 phero__h" data-hero-h>{p['title']}</h1>
      <p class="lead lead--i phero__d" data-hero-sub>{p['lead']}</p>
      <div class="hero__acts" data-hero-act>
        <a class="btn btn--pri" href="{base}index.html#contact" data-magnet="0.22"><span class="btn__t">Request a quotation</span>{ICON['arrow']}</a>
        <a class="btn btn--ghost-i" href="mailto:{EMAIL}" data-magnet="0.18"><span class="btn__t">{EMAIL}</span></a>
      </div>
    </div>
  </section>

  <section class="sec sec--paper">
    <div class="wrap two">
      <div class="rich">
        <p class="eyebrow" data-reveal>Product overview</p>
        {over}
        <h2 class="h3" style="margin-top:1.4rem" data-reveal>Benefits</h2>
        <ul class="ticks" data-stagger>{bens}</ul>
      </div>
      <aside class="aside" data-reveal>
        <h2 class="h4">Specifications</h2>
        <dl class="specs-tbl">{specs}</dl>
        <p style="font-size:.82rem;color:var(--t3)">Sizes, grades and finishes are confirmed against your drawings or a site survey before quotation.</p>
        <a class="tlink" href="{base}index.html#contact">Request a quotation{ICON['arr_sm']}</a>
      </aside>
    </div>
  </section>

  <section class="sec sec--white">
    <div class="wrap">
      <div class="shead">
        <div class="shead__top"><span class="shead__idx">{i+1:02d}</span><p class="eyebrow">Features</p></div>
        <div class="shead__grid">
          <h2 class="h2 shead__title" data-split>What you get as standard.</h2>
          <p class="lead" data-reveal>Six things included in every {plain.lower()} package we supply.</p>
        </div>
      </div>
      <div class="cards cards--3" data-stagger>{feats}</div>
    </div>
  </section>

  <section class="sec sec--paper">
    <div class="wrap">
      <div class="dim" style="margin-bottom:1.6rem">
        <span class="dim__txt">Gallery</span><span class="dim__line"></span><span class="dim__txt">{len(p['gallery'])} frames</span>
      </div>
      <div class="gal" data-stagger>{gal}</div>
    </div>
  </section>

  <section class="sec sec--white">
    <div class="wrap two">
      <div>
        <p class="eyebrow" data-reveal>Related products</p>
        <h2 class="h2" style="margin-top:1rem;max-width:22ch" data-split>Specified together more often than not.</h2>
      </div>
      <div class="aside" style="position:static" data-reveal>
        <div class="aside__list">{rel}</div>
        <a class="tlink" href="{base}index.html#products">All six product families{ICON['arr_sm']}</a>
      </div>
    </div>
  </section>

</main>
{cta(base, p['gallery'][1] if len(p['gallery']) > 1 else p['hero'],
     'Enquire', 'Tell us the sizes. We will price the ' + plain.lower() + '.',
     'Send drawings or an opening schedule, or ask us to survey the site. Quotations are free.')}
{footer(base)}'''


# ============================================================== PROJECT ===
def build_project(pr, i):
    base = '../'
    gal = ''.join(f'''
      <figure class="gal__i{' gal__i--w' if n == 0 else ''}" data-full="{base}assets/img/{g}-1400.jpg">
        <img src="{base}assets/img/{g}-800.jpg" alt="{html.unescape(pr['name'])} — {g.replace('-',' ')}" width="800" height="800" loading="lazy" decoding="async">
      </figure>''' for n, g in enumerate(pr['gallery']))

    plain = html.unescape(pr['name'])
    title = f'{pr["name"]} — {CO_SHORT} Reference Project'
    desc = html.unescape(pr['summary'])
    canon = f'{SITE}/projects/{pr["slug"]}.html'
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "CreativeWork", "name": plain, "url": canon, "description": desc,
         "image": f"{SITE}/assets/img/{pr['hero']}-1400.jpg",
         "about": {"@type": "Place", "name": html.unescape(pr['location'])},
         "author": {"@type": "Organization", "name": CO, "url": SITE + "/"}},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Projects", "item": SITE + "/#projects"},
            {"@type": "ListItem", "position": 3, "name": plain, "item": canon}]}]}

    return head(title, desc, canon, base, jsonld=ld) + shell_open(base) + nav(base) + f'''
<main id="main">

  <section class="phero">
    <div class="phero__bg" aria-hidden="true">
      <img src="{base}assets/img/{pr['hero']}-1400.jpg" alt="" width="1400" height="1400" fetchpriority="high" decoding="async" data-parallax="-8">
    </div>
    <div class="wrap phero__in">
      <nav class="crumbs" aria-label="Breadcrumb">
        <a href="{base}index.html">Home</a><span>/</span><a href="{base}index.html#projects">Projects</a><span>/</span><span style="opacity:1;color:var(--t2i)">{pr['name']}</span>
      </nav>
      <p class="eyebrow eyebrow--i" style="margin-top:1.4rem">Project {i+1:02d} of {len(PROJECTS)}</p>
      <h1 class="h1 phero__h" data-hero-h>{pr['name']}</h1>
      <p class="lead lead--i phero__d" data-hero-sub>{pr['location']} · {pr['status']}</p>
      <div class="hero__acts" data-hero-act>
        <a class="btn btn--pri" href="{base}index.html#contact" data-magnet="0.22"><span class="btn__t">Discuss a similar project</span>{ICON['arrow']}</a>
        <a class="btn btn--ghost-i" href="tel:{PHONE_H}" data-magnet="0.18"><span class="btn__t">{PHONE}</span></a>
      </div>
    </div>
  </section>

  <section class="sec sec--paper">
    <div class="wrap two">
      <div class="rich">
        <p class="eyebrow" data-reveal>Overview</p>
        <p data-reveal>{pr['summary']}</p>
      </div>
      <aside class="aside" data-reveal>
        <h3 class="h4">Project details</h3>
        <dl class="specs-tbl"><div><dt>Location</dt><dd>{pr['location']}</dd></div><div><dt>Main contractor</dt><dd>{pr['contractor']}</dd></div><div><dt>Client</dt><dd>{pr['client']}</dd></div><div><dt>Status</dt><dd><span class="tbl__st tbl__st--{'done' if pr['status']=='Completed' else 'soon'}">{pr['status']}</span></dd></div></dl>
        <a class="tlink" href="{base}index.html#projects">All projects{ICON['arr_sm']}</a>
      </aside>
    </div>
  </section>

  <section class="sec sec--white">
    <div class="wrap">
      <div class="dim" style="margin-bottom:1.6rem">
        <span class="dim__txt">Project gallery</span><span class="dim__line"></span><span class="dim__txt">{len(pr['gallery'])} frames</span>
      </div>
      <div class="gal" data-stagger>{gal}</div>
    </div>
  </section>

</main>
{cta(base, pr['gallery'][1] if len(pr['gallery']) > 1 else pr['hero'],
     'Enquire', 'Have a similar scope? Send the drawings and we will price it.',
     'Quotations are free. Give us the location, the programme dates and whatever drawings you have.')}
{footer(base)}'''


def build_gallery():
    gal = ''.join(f'''
      <figure class="gal__i{' gal__i--w' if i in (0, 9) else ''}" data-full="assets/img/{g}-1400.jpg">
        <img src="assets/img/{g}-800.jpg" alt="{a}" width="800" height="800" loading="lazy" decoding="async">
      </figure>''' for i, (g, a) in enumerate(GALLERY))

    title = f'Project Gallery — {CO_SHORT}, Dubai'
    desc = 'Fabrication and installation photography from ADSD Steel reference projects — structural steel, handrails and balustrades, access covers, cladding and bespoke metalwork.'
    canon = f'{SITE}/gallery.html'
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "ImageGallery", "name": "ADSD Steel Project Gallery", "url": canon, "description": desc},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Gallery", "item": canon}]}]}

    return head(title, desc, canon, jsonld=ld) + shell_open() + nav() + f'''
<main id="main">

  <section class="phero">
    <div class="phero__bg" aria-hidden="true">
      <img src="assets/img/mmw-stained-glass-staircase-1400.jpg" alt="" width="1400" height="1400" fetchpriority="high" decoding="async" data-parallax="-8">
    </div>
    <div class="wrap phero__in">
      <nav class="crumbs" aria-label="Breadcrumb">
        <a href="index.html">Home</a><span>/</span><span style="opacity:1;color:var(--t2i)">Gallery</span>
      </nav>
      <p class="eyebrow eyebrow--i" style="margin-top:1.4rem">Photography</p>
      <h1 class="h1 phero__h" data-hero-h>The full project gallery.</h1>
      <p class="lead lead--i phero__d" data-hero-sub>Structural steel, handrails and balustrades, access covers, cladding and bespoke metalwork — own fabrication and site work, drawn from our reference projects.</p>
      <div class="hero__acts" data-hero-act>
        <a class="btn btn--pri" href="index.html#contact" data-magnet="0.22"><span class="btn__t">Request a quotation</span>{ICON['arrow']}</a>
        <a class="btn btn--ghost-i" href="tel:{PHONE_H}" data-magnet="0.18"><span class="btn__t">{PHONE}</span></a>
      </div>
    </div>
  </section>

  <section class="sec sec--white">
    <div class="wrap">
      <div class="dim" style="margin-bottom:1.6rem">
        <span class="dim__txt">Gallery</span><span class="dim__line"></span><span class="dim__txt">{len(GALLERY)} frames</span>
      </div>
      <div class="gal" data-stagger>{gal}</div>
      <p class="cap" style="margin-top:1.2rem"><b>Note</b> All photography above is ADSD's own fabrication and site work.</p>
    </div>
  </section>

</main>
{cta('', 'ssf-canopy-entrance', 'Enquire',
     'Send drawings. Get a priced take-off.',
     'Quotations are free. Give us the location, the programme dates and whatever drawings you have.')}
{footer()}'''


# ============================================================== WRITE =====
def write(path, txt):
    with open(os.path.join(OUT, path), 'w', encoding='utf-8') as f:
        f.write(txt)

write('index.html', build_index())
write('gallery.html', build_gallery())
for i, s in enumerate(SERVICES):
    write(f'services/{s["slug"]}.html', build_service(s, i))
for i, p in enumerate(PRODUCTS):
    write(f'products/{p["slug"]}.html', build_product(p, i))
for i, pr in enumerate(PROJECTS):
    write(f'projects/{pr["slug"]}.html', build_project(pr, i))

# sitemap + robots
urls = [(SITE + '/', '1.0'), (SITE + '/gallery.html', '0.6')]
urls += [(f'{SITE}/services/{s["slug"]}.html', '0.8') for s in SERVICES]
urls += [(f'{SITE}/products/{p["slug"]}.html', '0.8') for p in PRODUCTS]
urls += [(f'{SITE}/projects/{pr["slug"]}.html', '0.7') for pr in PROJECTS]
write('sitemap.xml', '<?xml version="1.0" encoding="UTF-8"?>\n'
      '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
      + ''.join(f'  <url><loc>{u}</loc><priority>{p}</priority></url>\n' for u, p in urls)
      + '</urlset>\n')
write('robots.txt', f'User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n')

print(f'built 1 + {len(SERVICES)} + {len(PRODUCTS)} + {len(PROJECTS)} = '
      f'{1+len(SERVICES)+len(PRODUCTS)+len(PROJECTS)} pages')
