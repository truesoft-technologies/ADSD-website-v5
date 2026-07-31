#!/usr/bin/env python3
"""
build.py — generates the ADSD Steel Technical Services Contracting L.L.C site.

All company facts (services, projects, licences, contact details) are taken
verbatim from ADSD-COMPANY-PROFILE_-_Steel_Structure.pdf. Anything the profile
did not contain is written as industry-appropriate placeholder copy and listed
in CONTENT-NOTES.md.
"""
import os, json, html, shutil

OUT = '.'
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
    ('Services', '#services'),
    ('Products',   'all-products.html'),
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
        short='Primary frames, secondary steel and connections that are cut, drilled, welded and erected to approved shop drawings.',
        hero='prd-whatsapp-image-2026-07-21-at-12-01-21-1',
        lead='Primary and secondary structural steel, fabricated in our own workshop and erected on site by our own crews, from setting-out to final bolt-up.',
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
        short='Handrails, ladders, aluminium louvers, car parking sheds and substation chequer plate: the finishing steel.',
        hero='laser-metal-cutting',
        lead='The secondary metalwork that finishes a building: handrails, aluminium louvers, car parking sheds, substation chequer plate, ladders, gates and brackets.',
        body=[
            'The company profile groups this work as miscellaneous metal work, and it is usually the scope that decides whether a project feels finished. It is measured on site rather than scaled off a drawing, because openings, floor levels and kerb lines are never exactly where the design put them.',
            'Typical items include handrails and balustrades, aluminium louvers and screens, car parking sheds and canopies, substation chequer plate and access covers, cage ladders, gates, frames, grating and support brackets, fabricated to the measured dimension and installed by the same team.',
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
        short='Custom-fabricated steelwork engineered to the civil drawing: embedments, temporary works and site-specific metalwork made to order.',
        hero='prd-dewa-dubai-south-project-access-door',
        lead='Steel fabricated to the exact dimension a civil scope calls for: embedments, temporary works and access steel made to your drawing, not picked off a standard range.',
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
            ('Direct from the fabricator', 'No middleman mark-up between the drawing and the steel: priced and made in-house.'),
        ],
        specs=[
            ('Typical items', 'Embedded plates, anchor cages, temporary works steel, site railings, brackets'),
            ('Materials', 'Mild steel, galvanised steel, stainless steel on request'),
            ('Basis', 'Civil and structural drawings, site measurement, or the engineer design issued for the works'),
            ('Finishes', 'Primer, galvanised, or mill finish as specified'),
            ('Lead times', 'Prioritised against civil pour and programme dates'),
            ('Scope options', 'Supply only, or supply and fix on site'),
        ],
        gallery=['prd-dewa-dubai-south-project-access-door', 'site-warehouse-build', 'structure-crane-lift', 'steel-cutting'],
    ),
    dict(
        slug='tailor-made-fabrication-mep',
        title='Tailor-Made Fabrication Products for the MEP Sector',
        plain='Tailor-Made Fabrication Products for the MEP Sector',
        short='Custom steel supports, platforms and brackets fabricated to suit mechanical, electrical and plumbing installations.',
        hero='prd-elv-trench-panel',
        lead='Supports, platforms and brackets fabricated to fit the equipment, ductwork and containment an MEP contractor is actually installing, not a generic bracket range.',
        body=[
            'MEP installations carry steel that is rarely off the shelf: plant supports, duct hangers, cable tray ladder racks, pipe bridges, equipment platforms and drainage systems all need to match a specific layout. We fabricate these to your coordinated drawing, so the support is right the first time it reaches site.',
            'Drainage products are critical to MEP systems: grates and catch basins prevent debris from clogging pipes and manage surface water runoff, while trench drains, slot drains and French drains direct groundwater away from saturated areas. We fabricate these systems to coordinate with the wider MEP package and site conditions.',
            'Because the same workshop cuts, drills and welds every piece, changes that come out of a coordination meeting can be turned around quickly: a revised bracket, an extra hanger, or modified drain configuration does not have to wait behind a large order.',
        ],
        features=[
            ('Plant and equipment supports', 'Steel stands, cradles and frames fabricated to suit chillers, AHUs, pumps and packaged plant.'),
            ('Duct and cable tray supports', 'Hangers, trapezes and brackets sized to the coordinated services drawing.'),
            ('Pipe bridges and racks', 'Support steel for MEP pipe routes crossing plant rooms, risers and roof levels.'),
            ('Drainage systems and grates', 'Drainage grates and catch basins fabricated to manage surface water runoff, prevent debris entry, and maintain drainage system functionality.'),
            ('Access platforms', 'Maintenance platforms and walkways built around plant that needs to stay serviceable.'),
            ('Builders work coordination', 'Support steel detailed to coordinate with builders work openings and civil elements.'),
        ],
        benefits=[
            ('Fits the coordinated drawing', 'Supports are made to the services layout as coordinated, not a standard span table.'),
            ('One point of contact', 'Mechanical, electrical and plumbing support steel comes from a single fabricator.'),
            ('Responsive to site changes', 'Coordination revisions are turned around from the same workshop, not re-ordered from scratch.'),
            ('Finished for the environment', 'Coatings specified for plant rooms, roof exposure or corrosive environments as needed.'),
        ],
        specs=[
            ('Typical items', 'Plant stands, duct and pipe hangers, cable tray supports, access platforms, drainage grates, catch basins, trench drains, slot drains, floor drains, roof drains'),
            ('Drainage types', 'Gutter drains, downspouts, swale drains, trench drains, slot drains, shower drains, floor drains, balcony drains, roof drains, French drains'),
            ('Drainage systems', 'Catch basins to collect storm water and prevent flooding, French drains for water features and groundwater management'),
            ('Materials', 'Mild steel, galvanised steel, stainless steel on request'),
            ('Basis', 'Coordinated MEP shop drawings or site survey'),
            ('Finishes', 'Galvanised, powder coated, or primer and paint as specified'),
        ],
        gallery=['prd-elv-trench-panel', 'plant-steel-structure', 'silo-platform-access', 'tank-platform-crane'],
    ),
    dict(
        slug='tailor-made-fabrication-landscape-hospitality',
        title='Tailor-Made Fabrication Products for the Landscape &amp; Hospitality Industry',
        plain='Tailor-Made Fabrication Products for the Landscape and Hospitality Industry',
        short='Custom steel pergolas, shade structures and outdoor metalwork fabricated for landscape and hospitality projects.',
        hero='car-parking-shade-row',
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
        gallery=['prd-metal-car-shade', 'car-parking-shade-row', 'car-parking-shade-single', 'open-shed-structure'],
    ),
]

# ---------------------------------------------------------------- products --
PRODUCTS = [
    dict(
        slug='pre-engineered-steel-buildings',
        title='Pre-Engineered Steel Buildings',
        tag='Structures',
        short='Clear-span warehouses, workshops and industrial sheds with frames fabricated, clad and erected as one package.',
        hero='warehouse-exterior',
        lead='Clear-span portal-frame buildings for warehousing, workshops and light industry: engineered, fabricated, clad and erected as a single package.',
        overview=[
            'A pre-engineered building is the most efficient way to get covered industrial space onto a plot. The frame is designed around your required clear span and eaves height, fabricated as marked members in our workshop, then bolted together on site in a fraction of the time an in-situ structure would take.',
            'We supply the whole envelope: primary frames, purlins and side rails, bracing, roof and wall sheeting, insulation, gutters and downpipes, and the openings, including roller shutters, personnel doors, louvers and translucent roof lights. Mezzanine floors, crane gantries and office fit-out steel can be built into the same frame from the outset.',
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
        lead='Steel-framed shade structures for car parks, walkways and entrances, engineered for UAE sun, wind uplift and a finish that survives a coastal summer.',
        overview=[
            'Parking shades take more punishment than most people expect: forty-plus degrees of daily thermal cycling, wind uplift that tries to peel the covering off, and airborne salt working on every fixing. The frame therefore matters more than the fabric.',
            'We fabricate cantilever, single-post and back-to-back frames from hollow sections and plate, hot-dip galvanise or powder coat them, and set them on cast-in or post-installed base plates surveyed to the parking layout. The covering can be tensioned membrane, profiled sheet or insulated panel depending on the look, the budget and the maintenance you want to sign up for.',
        ],
        benefits=[
            ('Engineered for the uplift case', 'Sized for the wind load that actually fails Gulf shade structures, not just the dead weight.'),
            ('Finish that survives a coastal summer', 'Hot-dip galvanised or powder coated steelwork specified for salt and UV exposure.'),
            ('Bays stay usable', 'Bases set out against the surveyed parking layout, not the drawing, so columns land where cars actually park.'),
            ('Covering to match the budget', 'Tensioned membrane, profiled sheet or insulated panel, whichever suits the look and the maintenance you want.'),
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
        lead='Edge protection and access metalwork: stair handrails, platform balustrades, cage ladders and step-overs, fabricated to a site measurement so they fit first time.',
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
        lead='Weather louvers, privacy screens and plant enclosures, made to the measured opening, in aluminium or coated steel, with a bird mesh and a drainage detail that works.',
        overview=[
            'Louvers do two jobs at once: let air through and keep weather out. Getting both right is a matter of blade profile, pitch and the drainage path behind the blade, which is why an off-the-shelf panel cut down to size on site usually leaks.',
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
        lead='Chequer plate flooring, trench and pit covers, grating walkways and maintenance platforms, cut to the opening, framed, and safe to stand on.',
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
        lead='Roof and wall envelope work: profiled sheet, insulated sandwich panel, flashings, gutters and rainwater goods, supplied and fixed as one scope.',
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

# ------------------------------------------------------ product categories --
# Home-page product categories, each with its own dedicated page under
# products/. Every photo in ALL_PRODUCT_PHOTOS (defined further down) is
# assigned to exactly one category — Tailor Made Products picks up whatever
# the others don't claim.
_UPVC_SLUGS = [
    'prd-dry-gully-trap-upvc', 'prd-upvc-dry-manhole-cover', 'prd-upvc-fittings',
    'prd-grease-trap', 'prd-grease-trap-c-type', 'prd-grp-ladder-for-pump-room',
]
_HATCH_SLUGS = [
    'prd-access-hatch-1', 'prd-alain-municipality-park-access-hatch',
    'prd-basement-access-hatch-alain-municipality-project',
    'prd-dewa-dubai-south-project-access-door', 'prd-floor-access-hatch', 'prd-roof-access-hatch',
    'prd-wall-access-cover', 'prd-wall-access-panel', 'prd-floor-deck-cover-with-stone-infill',
    'prd-multi-cover-mhc-with-grp', 'prd-multi-tray-mhc',
    'prd-recessed-mhc', 'prd-solid-top-mhc', 'prd-meter-box', 'prd-elv-trench-panel',
    'prd-dubai-south-dewa-substation',
]
_KITCHEN_SLUGS = [
    # ducting
    'prd-kitchen-hood-duct', 'prd-water-duct-khood', 'prd-duct',
    'prd-whatsapp-image-2026-07-21-at-12-41-02-1',
    # kitchen & catering metalwork
    'prd-bainmarie', 'prd-bbq-outdoor-unit', 'prd-cafe-display-unit', 'prd-customized-mop-sink',
    'prd-etihad-dry-kitchen',
    'prd-etihad-hotkitchen', 'prd-etihad-staff-storage-cabinet', 'prd-etihad-staff-catering-storage-cabinet',
    'prd-hot-plate-with-burner', 'prd-janitorial-sink', 'prd-khawanij-private-villa-kitchen',
    'prd-kitchen-hood', 'prd-lazzat-kitchen-supplied-products',
    'prd-lazzat-resturant-in-karam', 'prd-lazzat-resturant-tandoor-kitchen',
    'prd-nouf-private-villa-kitchen', 'prd-nouf-private-villa-kitchen-2', 'prd-oil-pullout-tralley',
    'prd-private-villa-hot-kitchen', 'prd-resturant-in-al-zahia-c4', 'prd-resturant-in-al-zahia-mall',
    'prd-whatsapp-image-2026-07-21-at-13-03-13-1', 'prd-whatsapp-image-2026-07-21-at-13-03-13-2',
    'prd-whatsapp-image-2026-07-21-at-13-03-13',
    'prd-storage-unit-bbq-counter', 'prd-table-top-bbq-grill',
    'prd-mobile-trolley',
]
_HANDRAIL_SLUGS = [
    'prd-handrail-type-2', 'prd-handrain-3', 'prd-handrain-type-4', 'prd-balcony-balustard',
    'prd-balcony-fence', 'prd-swimming-pool-fence', 'prd-ramp-rail', 'prd-partician-rail',
    'prd-protection-guard', 'prd-cat-ladder', 'prd-metal-stair-case', 'prd-metal-stari-case-2',
    'prd-stair-case-type-1', 'prd-whatsapp-image-2026-07-21-at-12-01-21-1',
]
_DECORATIVE_SLUGS = [
    'prd-decorative-ac-grill', 'prd-decorative-bollard', 'prd-decorative-book-shelf',
    'prd-decorative-ceiling-feature', 'prd-decorative-customized-board', 'prd-decorative-display-shelf',
    'prd-decorative-screen-panel', 'prd-decorative-swimming-pool-handrail', 'prd-decorative-wall-design',
    'prd-decorative-water-feature', 'prd-decorative-window-panel', 'prd-laundry-cabinet-unit',
]
_DRAINAGE_SLUGS = [
    # gully & floor traps
    'prd-floor-gully-trap', 'prd-drainage-floor-drain-ss', 'prd-drainage-floor-trap',
    'prd-drainage-round-floor-drain', 'prd-drainage-catch-basin-cover',
    # floor & shower drains
    'prd-shower-drain', 'prd-showerdrain', 'prd-drainage-ss-recessed-drain',
    'prd-drainage-ss-slot-type-drain', 'prd-drainage-slotted-floor-drain',
    'prd-drainage-ss-floor-drain-cover', 'prd-drainage-ss-floor-cover',
    'prd-drainage-floor-drain-recessed', 'prd-drainage-balcony-drain',
    'prd-drainage-slotted-top-threaded-outlet',
    # slot & linear drains
    'prd-slot-drain', 'prd-water-feature-slot-drain', 'prd-radius-water-feature-linear-drain',
    'prd-drainage-radius-slot-drain', 'prd-drainage-linear-drain', 'prd-drainage-linear-slot-drain',
    'prd-drainage-double-slot-drain', 'prd-drainage-ss-double-slot-drain', 'prd-drainage-di-channel-ss-top',
    'prd-drainage-recessed-slotted-top', 'prd-drainage-ss-slotted-drain',
    # channel gratings
    'prd-drainage-amul-trap', 'prd-drainage-angle-frame-ladder-grating',
    'prd-drainage-angle-frame-non-slip-grating', 'prd-drainage-angle-frame-slotted-top',
    'prd-drainage-channel-grating', 'prd-drainage-channel-heel-guard',
    'prd-drainage-channel-non-slip-grating', 'prd-drainage-heavy-duty-grating',
    'prd-drainage-ladder-type-grating', 'prd-drainage-ss-ladder-grating-frame',
    'prd-drainage-industrial-floor-grating', 'prd-pool-linear-gratings', 'prd-ablution-gratings',
    # rain water outlets & clean-outs
    'prd-drainage-ss-rain-water-outlet', 'prd-drainage-alu-clean-out',
    'prd-drainage-powder-coated-clean-out', 'prd-drainage-roof-drain',
    'prd-drainage-rain-water-outlet-round', 'prd-drainage-ss-flap-type-drain',
    'prd-drainage-scrupper-drain', 'prd-drainage-slotted-drain-outlet', 'prd-drainage-parapet-drain',
]

PRODUCT_CATEGORIES = [
    dict(
        slug='upvc', title='UPVC', tag='Drainage &amp; fittings', hero='prd-dry-gully-trap-upvc',
        short='UPVC gully traps, grease traps, manhole covers and drainage fittings made and installed to the drawing.',
        lead='UPVC drainage components fabricated and installed to the drawing: gully traps, grease traps, manhole covers, slot drains and fitting work for kitchens, plant rooms and external drainage runs.',
        overview=[
            'UPVC is specified wherever a drainage run needs to resist grease, chemicals or constant moisture without corroding. We fabricate and install gully traps, grease traps, manhole covers and drainage fittings to the site drawing, matched to the pipe sizes and invert levels already on site.',
            'Work covers everything from a single replacement trap to a full kitchen or plant-room drainage package, tied into the wider civil or MEP drainage network being installed on the same project.',
        ],
        benefits=[
            ('Matched to the pipe run', 'Fittings are sized to the actual pipe diameters and invert levels on site, not a generic catalogue size.'),
            ('Resists grease and chemicals', 'UPVC holds up in kitchen and plant-room drainage where metal fittings corrode.'),
            ('Covers set flush', 'Manhole and gully covers are set to finish flush with the surrounding floor or paving.'),
            ('Tied into the wider drainage package', 'Fittings are coordinated with the civil or MEP drainage scope on the same project.'),
        ],
        specs=[
            ('Typical items', 'Gully traps, grease traps, manhole and gully covers, slot drains, pipe fittings'),
            ('Materials', 'UPVC, with stainless steel or galvanised covers and frames where specified'),
            ('Basis', 'Site-measured against the drawing and the as-built pipe run'),
            ('Finishes', 'Mill finish UPVC, with painted or galvanised metal covers and frames'),
            ('Applications', 'Commercial kitchens, plant rooms, external drainage, landscape water features'),
            ('Scope options', 'Supply only, or supply and install on site'),
        ],
        features=[
            ('Gully traps', 'Floor-mounted UPVC gully traps sized to the drainage run and finished flush with the floor.'),
            ('Grease traps', 'C-type and standard grease traps fabricated for commercial kitchen drainage.'),
            ('Manhole and gully covers', 'UPVC and stainless steel covers set flush to the surrounding surface.'),
            ('Slot and linear drains', 'Channel drains and linear slot drains for floors, plant rooms and water features.'),
            ('Pipe fittings', 'Junctions, reducers and fittings made to the pipe sizes on the drawing.'),
            ('Site-measured installation', 'Every item is checked against the as-built pipe run before it is fixed.'),
        ],
        noun='UPVC',
        photos=_UPVC_SLUGS,
    ),
    dict(
        slug='drainage-products', title='Drainage Products', tag='Drainage &amp; gratings', hero='prd-floor-gully-trap',
        short='Floor and shower drains, slot and linear drains, channel gratings and rain water outlets, fabricated to the drainage run.',
        lead='Floor traps, slot and linear drains, channel gratings and rain water outlets installed over a drainage system to carry water away and keep debris out, sized and finished to the drawing.',
        overview=[
            'Drainage products sit at the point where a floor, roof, balcony or channel meets the wider drainage network: gully and floor traps, slot and linear drains, channel gratings and rain water outlets that carry water away while keeping debris out of the pipe run.',
            'The range covers everything from a single recessed shower drain to a full car park or roof drainage package: catch basins and gully traps at the collection point, channel and slot drains along the run, and rain water outlets, scuppers and clean-outs where the water leaves the building.',
        ],
        benefits=[
            ('Matched to the drainage run', 'Traps, drains and outlets are sized to the pipe run and invert levels already on site, not a generic catalogue size.'),
            ('Keeps debris out', 'Gratings and covers are selected to stop leaves, grit and site debris entering the drainage system while still passing the design flow.'),
            ('Covers and gratings set flush', 'Floor, channel and roof-level items are set to finish flush with the surrounding surface or paving.'),
            ('One supplier for the whole run', 'Collection points, channel drains and outlets are coordinated so the same fabricator carries the drainage package end to end.'),
        ],
        specs=[
            ('Typical items', 'Gully and floor traps, catch basins, slot and linear drains, channel gratings, rain water outlets, scuppers, clean-outs'),
            ('Materials', 'Stainless steel, galvanised steel, ductile iron, with UPVC or GRP components where specified'),
            ('Basis', 'Site-measured against the drawing and the as-built invert levels'),
            ('Finishes', 'Mill finish or brushed stainless, galvanised, powder coated'),
            ('Applications', 'Bathrooms, balconies, car parks, roofs, plant rooms, landscape and water features'),
            ('Scope options', 'Supply only, or supply and install on site'),
        ],
        features=[
            ('Gully and floor traps', 'Floor-mounted traps and catch basins sized to the drainage run and finished flush with the floor.'),
            ('Shower and floor drains', 'Recessed, slotted and round floor drains for bathrooms, balconies and plant areas.'),
            ('Slot and linear drains', 'Channel and linear slot drains, including radius trims for water features, sized to the flow rate.'),
            ('Channel gratings', 'Heavy-duty, ladder-type, non-slip and heel-guard gratings for car parks, plant rooms and public floors.'),
            ('Rain water outlets', 'Roof drains, parapet drains, scuppers and clean-outs in stainless steel, aluminium or powder-coated finish.'),
            ('Site-measured installation', 'Every item is checked against the as-built pipe run and invert level before it is fixed.'),
        ],
        noun='drainage',
        photos=_DRAINAGE_SLUGS,
    ),
    dict(
        slug='access-hatch-cover', title='Access Hatch Cover', tag='Access &amp; covers', hero='prd-access-hatch-1',
        short='Floor, roof, wall and basement access hatches and covers, sized to the opening and finished to match the surrounding surface.',
        lead='Floor, roof, wall and basement access hatches and covers, sized to the opening and finished to match the surrounding surface, with manhole covers and trench panels for the same access requirement.',
        overview=[
            'Access hatches and covers exist to disappear into whatever surface they sit in and open cleanly the one time a year someone actually needs them. Every hatch is measured against the finished opening, not the design dimension, and fitted with gas struts, locking handles and safety chains sized to the weight of the cover.',
            'The range covers floor, roof, wall and basement hatches, chequer plate and stone-infill covers, and the manhole and trench covers that sit alongside them on the same project.',
        ],
        benefits=[
            ('Sized to the finished opening', 'Hatches are measured against the as-built opening, not the design drawing, so they sit flush.'),
            ('Gas struts and locking hardware', 'Stays, handles and safety chains are sized to the weight of the cover being lifted.'),
            ('Finished to match the surface', 'Stone, chequer plate or paint finish is matched to what surrounds the hatch.'),
            ('One crew for hatches and covers', 'Roof hatches, floor hatches and manhole covers on the same project come from the same fabricator.'),
        ],
        specs=[
            ('Typical items', 'Floor, roof, wall and basement access hatches, manhole covers, trench and duct covers'),
            ('Materials', 'Mild steel, stainless steel, GRP, with stone or chequer plate infill on request'),
            ('Hardware', 'Gas struts, locking handles, safety chains and stainless hinges'),
            ('Finishes', 'Powder coated, galvanised, or finished to match the surrounding surface'),
            ('Basis', 'Site-measured against the finished opening'),
            ('Scope options', 'Supply only, or supply and install on site'),
        ],
        features=[
            ('Floor access hatches', 'Recessed hatches set into a waterproofed upstand, finished flush with the floor.'),
            ('Roof access hatches', 'Factory-finished roof hatches with gas-strut stays and a weathertight seal.'),
            ('Wall access panels', 'Flush wall panels for service ducts and risers, hinged or lift-off.'),
            ('Basement and pit hatches', 'Heavier-duty hatches for basement, pit and plant-room access.'),
            ('Manhole and trench covers', 'Chequer plate and solid-top covers sized to the opening and the imposed load.'),
            ('Locking and safety hardware', 'Handles, stays and chains sized to the cover weight and the access frequency.'),
        ],
        noun='access hatch cover',
        photos=_HATCH_SLUGS,
    ),
    dict(
        slug='customized-kitchen', title='Customized Kitchen Products', tag='Hospitality &amp; catering', hero='prd-kitchen-hood',
        short='Commercial kitchen and catering metalwork made to the equipment schedule: hoods, worktops, sinks and storage.',
        lead='Commercial kitchen and catering metalwork made to the equipment schedule: extraction hoods and ducting, worktops, sinks, storage and display units for restaurants, hotels and staff catering facilities.',
        overview=[
            'A commercial kitchen is fitted around the equipment that goes into it, not the other way round, so extraction hoods, worktops, sinks and storage are fabricated to the equipment schedule and the kitchen consultant drawing rather than picked from a catalogue.',
            'The scope covers everything from a single extraction hood to a full back-of-house fit-out: hoods and ducting, cooking line worktops, wash-up sinks, staff storage and front-of-house display and BBQ units.',
        ],
        benefits=[
            ('Built to the equipment schedule', 'Hoods, worktops and sinks are sized to the actual cooking line and equipment being installed.'),
            ('Extraction that meets the airflow spec', 'Hoods and ducting are sized and fixed to the extraction rate the kitchen consultant specifies.'),
            ('Finished for food-safety inspection', 'Stainless steel welds and seams are finished to pass a food-safety inspection.'),
            ('One fit-out, one contractor', 'Hoods, worktops, sinks and storage for the same kitchen come from a single workshop.'),
        ],
        specs=[
            ('Typical items', 'Extraction hoods and ducting, worktops, sinks, storage cabinets, display and BBQ units'),
            ('Materials', 'Stainless steel throughout, with decorative panel finishes on customer-facing units'),
            ('Basis', 'Kitchen consultant drawing or a site-measured equipment schedule'),
            ('Finishes', 'Brushed or mirror stainless steel, with a decorative pattern-cut option'),
            ('Applications', 'Restaurants, hotel kitchens, staff catering facilities, cafe and mall display units'),
            ('Scope options', 'Supply only, or supply and install on site'),
        ],
        features=[
            ('Extraction hoods and ducting', 'Hoods sized to the cooking line and ducted to the extraction rate specified.'),
            ('Cooking line worktops', 'Stainless steel worktops and stands built around the equipment schedule.'),
            ('Sinks and wash-up units', 'Pot wash, hand wash and mop sinks finished for continuous commercial use.'),
            ('Staff catering and storage', 'Storage cabinets, lockers and catering units for staff and back-of-house areas.'),
            ('Display and front-of-house units', 'Cafe and display counters finished for customer-facing areas.'),
            ('BBQ and outdoor cooking units', 'Outdoor BBQ counters and grill units built for continuous outdoor use.'),
        ],
        noun='customized kitchen',
        photos=_KITCHEN_SLUGS,
    ),
    dict(
        slug='all-handrail', title='Balustrades &amp; Handrails', tag='Access &amp; safety', hero='prd-handrain-3',
        short='Stair, ramp, balcony and pool handrails and balustrades, fabricated to a site measurement.',
        lead='Stair, ramp, balcony and pool handrails and balustrades, fabricated to a site measurement in tube, box section, glass-infill or stainless steel, with the ladders and stair fabrication that go alongside them.',
        overview=[
            'A handrail is a safety item and the last thing installed before an inspection, which is why it is measured on site rather than scaled off the drawing: slab edges move, stair rises get adjusted, and a rail made to the design dimension often arrives short.',
            'The range covers stair and ramp handrails, balcony balustrades and pool fencing, plus the cage ladders and stair fabrication that share the same measured, site-fitted approach.',
        ],
        benefits=[
            ('Measured, not assumed', 'Every run is set out from the as-built structure, which is why it fits first time.'),
            ('Passes inspection first time', 'Fabricated as a safety item to the standard the inspector is actually checking against.'),
            ('Matched to the application', 'Pool fencing, balcony balustrades and stair rails each get the fixing and finish that application needs.'),
            ('Ladders and stairs from the same crew', 'Handrails, cage ladders and stair fabrication on one project come from a single fabricator.'),
        ],
        specs=[
            ('Typical items', 'Stair and ramp handrails, balcony balustrades, pool fencing, cage ladders'),
            ('Materials', 'Stainless steel, galvanised tube, box section, with glass infill on request'),
            ('Fixing', 'Base-plated, side-fixed or core-drilled, with self-closing gates for pool fencing'),
            ('Finishes', 'Mirror or brushed stainless, powder coated, hot-dip galvanised'),
            ('Basis', 'Site survey and measurement before fabrication'),
            ('Scope options', 'Supply only, or supply and install on site'),
        ],
        features=[
            ('Stair and landing handrails', 'Tube and box-section rails with returns and continuous top rails, fitted to the measured stair.'),
            ('Balcony balustrades', 'Glass-infill and bar balustrades fabricated to the balcony edge condition.'),
            ('Pool safety fencing', 'Self-closing gates and fencing built to pool safety requirements.'),
            ('Ramp handrails', 'Continuous rails fixed to accessible ramps at the required height and projection.'),
            ('Cage ladders', 'Fixed vertical ladders with safety cages for roof and plant access.'),
            ('Stair fabrication', 'Steel stair frames and treads fabricated and erected alongside the handrail package.'),
        ],
        noun='handrail',
        photos=_HANDRAIL_SLUGS,
    ),
    dict(
        slug='decorative-products', title='Decorative Products', tag='Design &amp; finishes', hero='prd-decorative-wall-design',
        short='Architectural metalwork, feature screens, ceiling designs, wall panels and bespoke decorative installations.',
        lead='Decorative screens, enclosures, water tanks, planters and one-off fabrication built to a design rather than picked from a standard range, for villas, retail and industrial projects across the UAE.',
        overview=[
            'Not every request fits a standard product line. This is the bespoke and one-off work: decorative screens and panels, plant and meter enclosures, GRP water tanks, planters and villa metalwork, built to a design or a site measurement rather than a catalogue part.',
            'Because it comes from the same workshop as our structural and secondary steel, one-off items are detailed to sit correctly against whatever they are fixed to, and finished to be seen rather than just to hold together.',
        ],
        benefits=[
            ('Built to the design, not a catalogue', 'Every piece is fabricated to a supplied design or a site measurement.'),
            ('Finish-first fabrication', 'Welds, edges and coatings are finished to be seen, not just to hold load.'),
            ('One workshop, any item', 'From a single decorative screen to a full villa metalwork package.'),
            ('Matched to the rest of the works', 'Bespoke items are detailed to sit correctly against the structure or finishes around them.'),
        ],
        specs=[
            ('Typical items', 'Decorative screens and panels, enclosures, GRP water tanks, planters, villa metalwork'),
            ('Materials', 'Mild steel, stainless steel, brass, aluminium, GRP'),
            ('Basis', 'Supplied design, architect drawing, or a site-measured concept'),
            ('Finishes', 'Powder coated, plated, brushed or mirror metal, feature paint finishes'),
            ('Applications', 'Private villas, retail and hospitality fit-outs, plant and utility enclosures'),
            ('Scope options', 'Supply only, or supply and install on site'),
        ],
        features=[
            ('Decorative screens and panels', 'CNC-cut and fretwork screens, room dividers and wall displays built to a design.'),
            ('Plant and meter enclosures', 'Enclosures and cages sized to the equipment they protect.'),
            ('GRP water tanks', 'Sectional GRP water tanks and tank-room ladders fabricated and installed.'),
            ('Villa and landscape metalwork', 'Gates, canopies, car shades and feature metalwork for private villas.'),
            ('Planters and site furniture', 'Planters, tree grates and outdoor furniture frames built to the landscape design.'),
            ('One-off fabrication', 'Anything else that does not fit a standard product line, built to your drawing or design.'),
        ],
        noun='decorative',
        photos=_DECORATIVE_SLUGS,
    ),
    dict(
        slug='tailor-made-products', title='Tailor Made Products', tag='Custom fabrication', hero='prd-tme-outdoor-light-box',
        short='One-off metalwork, custom enclosures, decorative screens, planters and bespoke site-specific fabrication.',
        lead='Custom one-off fabrication beyond standard product ranges: decorative screens, enclosures, planters, villa metalwork and anything else that does not fit a standard product line, built to your drawing or design.',
        overview=[
            'Bespoke fabrication is where standard categories stop. If it sits outside the scope of our defined product lines but uses the same materials, processes and fabrication capability, we take it on and deliver it to the same standard and programme as any other project.',
            'Applications range from decorative screens and feature metalwork to plant enclosures, meter boxes, planters and site-specific fabrication. Every item is built to a supplied design, an architect drawing, or a concept we develop with you on site.',
        ],
        benefits=[
            ('One-off capability', 'Anything outside standard product lines is built to the same specification and quality standard.'),
            ('Flexible scope', 'Supplied design, architect drawing, or a site-measured concept and we fabricate to suit.'),
            ('Material and finish range', 'Mild steel, stainless steel, brass, aluminium, GRP—with plating, powder coating or feature finishes.'),
            ('Integrated with main scope', 'Where these items sit inside a larger project, they are detailed to match the main structural steel or metalwork contract.'),
        ],
        specs=[
            ('Typical items', 'Decorative screens and panels, enclosures, GRP water tanks, planters, villa metalwork'),
            ('Materials', 'Mild steel, stainless steel, brass, aluminium, GRP'),
            ('Basis', 'Supplied design, architect drawing, or a site-measured concept'),
            ('Finishes', 'Powder coated, plated, brushed or mirror metal, feature paint finishes'),
            ('Applications', 'Private villas, retail and hospitality fit-outs, plant and utility enclosures'),
            ('Scope options', 'Supply only, or supply and install on site'),
        ],
        features=[
            ('Decorative screens and panels', 'CNC-cut and fretwork screens, room dividers and wall displays built to a design.'),
            ('Plant and meter enclosures', 'Enclosures and cages sized to the equipment they protect.'),
            ('GRP water tanks', 'Sectional GRP water tanks and tank-room ladders fabricated and installed.'),
            ('Villa and landscape metalwork', 'Gates, canopies, car shades and feature metalwork for private villas.'),
            ('Planters and site furniture', 'Planters, tree grates and outdoor furniture frames built to the landscape design.'),
            ('One-off fabrication', 'Anything else that does not fit a standard product line, built to your drawing or design.'),
        ],
        noun='tailor-made',
        photos=[],  # filled in below once ALL_PRODUCT_PHOTOS exists — everything the other five don't claim
    ),
]

# ---------------------------------------------------------------- projects --
# Reference-project photographs, shown as a card grid on the home page (no
# dedicated detail pages). (slug, name, location) — name/location as given.
PROJECTS = [
    ('proj-aecom-site-silicon-oasis', 'Aecom Site Dubai Silicon Oasis', 'Dubai, UAE'),
    ('proj-al-ain-municipality-park', 'Municipality Park', 'Al Ain, UAE'),
    ('proj-cladding-in-a-restaurant-al-zahia-mall', 'Restaurant', 'Al Zahia Mall, UAE'),
    ('proj-dubai-south-dewa-station', 'Dubai DEWA Station', 'Dubai, UAE'),
    ('proj-lazzat-restaurant-in-karama-dubai', 'Lazzat Restaurant', 'Dubai, UAE'),
    ('proj-private-villa-in-pearl-jumeirah', 'Private Villa', 'Pearl Jumeirah, Dubai, UAE'),
    ('proj-private-villa-kitchen-al-qusais', 'Private Villa Kitchen', 'Dubai, UAE'),
    ('proj-private-villa-hot-kitchen-emirates-hills', 'Private Villa Hot Kitchen', 'Dubai, UAE'),
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

    # ---- product photography, drawn from ALL_PRODUCT_PHOTOS below ----
    ('prd-ablution-gratings', 'Decorative ablution gratings with brass surround, floor drain'),
    ('prd-balcony-balustard', 'Horizontal-fin balustrade at a villa entrance'),
    ('prd-balcony-fence', 'Horizontal-fin balcony screen and guarding'),
    ('prd-kitchen-hood', 'Patterned stainless steel kitchen extraction hood'),
    ('prd-kitchen-hood-duct', 'Kitchen extraction ducting fixed to a building facade'),
    ('prd-metal-car-shade', 'Steel-framed car shade over a villa driveway'),
    ('prd-handrain-3', 'Stainless steel and glass stair handrail, on site'),
    ('prd-cat-ladder', 'Fixed cat ladder to a workshop roof'),
    ('prd-grp-water-tank', 'GRP sectional water tank, plant room'),
    ('prd-grp-ladder-for-pump-room', 'GRP ladder fitted inside a pump room access hatch'),
    ('prd-access-hatch-1', 'Factory-finished steel access hatch, hinge and stay detail'),
    ('prd-floor-access-hatch', 'Floor access hatch set into a waterproofed upstand'),
    ('prd-elv-trench-panel', 'Chequer plate trench covers, ready for installation'),
    ('prd-protection-guard', 'Stainless bollard guards at an escalator landing'),
    ('prd-swimming-pool-fence', 'Stainless steel pool safety fence and self-closing gate'),
    ('prd-tree-grate', 'Decorative sunburst tree grate, mall floor'),
    ('prd-slot-drain', 'Linear slot drain channel, workshop finish'),
    ('prd-basement-access-hatch-alain-municipality-project', 'Basement access hatch, Al Ain municipality project'),
    ('prd-whatsapp-image-2026-07-21-at-12-01-21-1', 'Fabricated steel staircase frame under construction'),
    ('prd-wall-access-panel', 'Flush wall access panel, service duct'),
    ('prd-roof-access-hatch', 'Roof access hatch, factory finished'),
    ('prd-radius-water-feature-linear-drain', 'Radius linear drain trim for a water feature, on site'),
]

# ------------------------------------------------------- all-products page --
# All 106 usable photos from the product reference folder ("D:\Grease Trap
# C type drwg" — misleadingly named; it holds mixed product photography, not
# just grease traps). One .mp4 in that folder is not an image and is excluded.
# (slug, title) — files copied in as assets/img/{slug}-800.jpg / -1400.jpg.
ALL_PRODUCT_PHOTOS = [
    ('prd-upvc-dry-manhole-cover', 'UPVC Dry Manhole Cover'),
    ('prd-decorative-ac-grill', 'Decorative AC Grille'),
    ('prd-nouf-private-villa-kitchen-2', 'Nouf Private Villa Kitchen'),
    ('prd-whatsapp-image-2026-07-21-at-13-03-13', 'Restaurant Kitchen Hood Installation'),
    ('prd-etihad-staff-catering-storage-cabinet', 'Etihad Staff Catering Storage Cabinet'),
    ('prd-grp-water-tank', 'GRP Water Tank'),
    ('prd-lazzat-resturant-tandoor-kitchen', 'Lazzat Restaurant Tandoor Kitchen'),
    ('prd-ablution-gratings', 'Ablution Gratings'),
    ('prd-metal-door-miniature', 'Metal Door Miniature'),
    ('prd-handrain-type-4', 'Handrail Type'),
    ('prd-enclosure', 'Enclosure'),
    ('prd-recessed-mhc', 'Recessed MHC'),
    ('prd-balcony-balustard', 'Balcony Balustrade'),
    ('prd-solid-top-mhc', 'Solid Top MHC'),
    ('prd-tree-grate', 'Tree Grate'),
    ('prd-pool-linear-gratings', 'Pool Linear Gratings'),
    ('prd-floor-gully-trap', 'Floor Gully Trap'),
    ('prd-lazzat-resturant-in-karam', 'LAZZAT Restaurant In Karam'),
    ('prd-villa-in-khawaneej', 'Villa In Khawaneej'),
    ('prd-metal-stari-case-2', 'Metal Stair Case'),
    ('prd-dry-gully-trap-upvc', 'Dry Gully Trap UPVC'),
    ('prd-water-feature-slot-drain', 'Water Feature Slot Drain'),
    ('prd-dubai-hill-mall-display-unit-olab-cafe', 'Dubai Hill Mall Display Unit Olab Cafe'),
    ('prd-dubai-south-dewa-substation', 'Dubai South - DEWA Substation'),
    ('prd-meter-box', 'Meter Box'),
    ('prd-ramp-rail', 'Ramp Rail'),
    ('prd-whatsapp-image-2026-07-21-at-12-01-21-1', 'Metal Staircase Fabrication'),
    ('prd-kitchen-hood', 'Kitchen Hood'),
    ('prd-resturant-in-al-zahia-c4', 'Restaurant In Al Zahia C4'),
    ('prd-multi-tray-mhc', 'Multi Tray MHC'),
    ('prd-kitchen-hood-duct', 'Kitchen Hood Duct'),
    ('prd-dunage-trolley', 'Dunnage Trolley'),
    ('prd-majilis-meal-screen', 'Majlis Meal Screen'),
    ('prd-display-unit', 'Display Unit'),
    ('prd-elv-trench-panel', 'ELV Trench Panel'),
    ('prd-basement-access-hatch-alain-municipality-project', 'Basement Access Hatch - Alain Municipality Project'),
    ('prd-grp-water-tank1', 'GRP Water Tank'),
    ('prd-balcony-fence', 'Balcony Fence'),
    ('prd-door-screen', 'Door Screen'),
    ('prd-alain-municipality-park-access-hatch', 'Alain Municipality Park Access Hatch'),
    ('prd-whatsapp-image-2026-07-21-at-13-03-13-1', 'Restaurant Kitchen Hood Installation'),
    ('prd-center-table', 'Center Table'),
    ('prd-janitorial-sink', 'Janitorial Sink'),
    ('prd-enclosure-3', 'Enclosure'),
    ('prd-water-duct-khood', 'Water Duct - Kitchen Hood'),
    ('prd-metal-canopy', 'Metal Canopy'),
    ('prd-floor-deck-cover-with-stone-infill', 'Floor Deck Cover With Stone Infill'),
    ('prd-swimming-pool-fence', 'Swimming Pool Fence'),
    ('prd-metal-stair-case', 'Metal Stair Case'),
    ('prd-etihad-dry-kitchen', 'Etihad - Dry Kitchen'),
    ('prd-private-villa-in-rahmaniya', 'Private Villa In Rahmaniya'),
    ('prd-lazzat-kitchen-supplied-products', 'Lazzat Kitchen Supplied Products'),
    ('prd-wall-access-cover', 'Wall Access Cover'),
    ('prd-grp-watertank-ladder', 'GRP Water Tank Ladder'),
    ('prd-bbq-outdoor-unit', 'BBQ Outdoor Unit'),
    ('prd-handrain-3', 'Handrail Type'),
    ('prd-khawanij-private-villa-kitchen', 'Khawanij Private Villa - Kitchen'),
    ('prd-duct', 'Duct'),
    ('prd-whatsapp-image-2026-07-21-at-13-03-13-2', 'Restaurant Kitchen Hood Installation'),
    ('prd-private-villa-hot-kitchen', 'Private Villa Hot Kitchen'),
    ('prd-access-hatch-1', 'Access Hatch'),
    ('prd-resturant-in-al-zahia-mall', 'Restaurant In Al Zahia Mall'),
    ('prd-storage-unit-bbq-counter', 'Storage Unit - BBQ Counter'),
    ('prd-socet-enclosure', 'Socket Enclosure'),
    ('prd-skirting-profile', 'Skirting Profile'),
    ('prd-etihad-staff-storage-cabinet', 'Etihad Staff - Storage Cabinet'),
    ('prd-wall-cabinet', 'Wall Cabinet'),
    ('prd-grease-trap-c-type', 'Grease Trap C Type'),
    ('prd-metal-cage', 'Metal Cage'),
    ('prd-partician-rail', 'Partition Rail'),
    ('prd-nouf-private-villa-kitchen', 'Nouf Private Villa Kitchen'),
    ('prd-radius-water-feature-linear-drain', 'Radius Water Feature Linear Drain'),
    ('prd-dewa-dubai-south-project-access-door', 'DEWA Dubai South Project - Access Door'),
    ('prd-grp-ladder-for-pump-room', 'GRP Ladder For Pump Room'),
    ('prd-showerdrain', 'Showerdrain'),
    ('prd-cafe-display-unit', 'Cafe Display Unit'),
    ('prd-staff-locker-cabinet', 'Staff Locker Cabinet'),
    ('prd-whatsapp-image-2026-07-21-at-12-41-02-1', 'Wall-Mounted Duct Enclosure'),
    ('prd-etihad-hotkitchen', 'Etihad - Hot Kitchen'),
    ('prd-slot-drain', 'Slot Drain'),
    ('prd-shower-drain', 'Shower Drain'),
    ('prd-multi-cover-mhc-with-grp', 'Multi Cover MHC With GRP'),
    ('prd-customized-mop-sink', 'Customized Mop Sink'),
    ('prd-bainmarie', 'Bain Marie'),
    ('prd-wall-access-panel', 'Wall Access Panel'),
    ('prd-khawanij-private-villa', 'Khawanij Private Villa'),
    ('prd-stair-case-type-1', 'Stair Case Type'),
    ('prd-roof-access-hatch', 'Roof Access Hatch'),
    ('prd-protection-guard', 'Protection Guard'),
    ('prd-wall-enclosure-2', 'Wall Enclosure'),
    ('prd-enclosure-4', 'Enclosure'),
    ('prd-handrail-type-2', 'Handrail Type'),
    ('prd-table-top-bbq-grill', 'Table Top BBQ Grill'),
    ('prd-floor-access-hatch', 'Floor Access Hatch'),
    ('prd-hot-plate-with-burner', 'Hot Plate With Burner'),
    ('prd-mobile-trolley', 'Mobile Trolley'),
    ('prd-upvc-fittings', 'UPVC Fittings'),
    ('prd-cat-ladder', 'Cat Ladder'),
    ('prd-oil-pullout-tralley', 'Oil Pullout Trolley'),
    ('prd-grease-trap', 'Grease Trap'),
    ('prd-decorative-ac-grill', 'Decorative AC Grill'),
    ('prd-decorative-bollard', 'Decorative Bollard'),
    ('prd-decorative-book-shelf', 'Decorative Book Shelf'),
    ('prd-decorative-ceiling-feature', 'Decorative Ceiling Feature'),
    ('prd-decorative-customized-board', 'Decorative Customized Board'),
    ('prd-decorative-display-shelf', 'Decorative Display Shelf'),
    ('prd-decorative-screen-panel', 'Decorative Screen Panel'),
    ('prd-decorative-swimming-pool-handrail', 'Decorative Swimming Pool Handrail'),
    ('prd-decorative-wall-design', 'Decorative Wall Design'),
    ('prd-decorative-water-feature', 'Decorative Water Feature'),
    ('prd-decorative-window-panel', 'Decorative Window Panel'),
    ('prd-laundry-cabinet-unit', 'Laundry Cabinet Unit'),

    # ---- Drainage Products (Tailor-Made-Drainage reference folder) ----
    ('prd-drainage-floor-drain-ss', 'Floor Drain SS'),
    ('prd-drainage-floor-trap', 'Floor Trap'),
    ('prd-drainage-round-floor-drain', 'Round Floor Drain'),
    ('prd-drainage-catch-basin-cover', 'Catch Basin Cover'),
    ('prd-drainage-ss-recessed-drain', 'SS Recessed Drain'),
    ('prd-drainage-ss-slot-type-drain', 'SS Slot Type Drain'),
    ('prd-drainage-slotted-floor-drain', 'Slotted Floor Drain'),
    ('prd-drainage-ss-floor-drain-cover', 'SS Floor Drain Cover'),
    ('prd-drainage-ss-floor-cover', 'SS Floor Cover'),
    ('prd-drainage-floor-drain-recessed', 'Floor Drain Recessed'),
    ('prd-drainage-balcony-drain', 'Balcony Drain'),
    ('prd-drainage-slotted-top-threaded-outlet', 'Slotted Top Threaded Outlet'),
    ('prd-drainage-radius-slot-drain', 'Radius Type Slot Drain'),
    ('prd-drainage-linear-drain', 'Linear Drain'),
    ('prd-drainage-linear-slot-drain', 'Linear Slot Drain'),
    ('prd-drainage-double-slot-drain', 'Double Slot Drain'),
    ('prd-drainage-ss-double-slot-drain', 'SS Double Slot Drain'),
    ('prd-drainage-di-channel-ss-top', 'DI Channel With SS Top'),
    ('prd-drainage-recessed-slotted-top', 'Recessed Slotted Top'),
    ('prd-drainage-ss-slotted-drain', 'SS Slotted Drain'),
    ('prd-drainage-amul-trap', 'Amul Trap'),
    ('prd-drainage-angle-frame-ladder-grating', 'Angle Frame With Ladder Type Grating'),
    ('prd-drainage-angle-frame-non-slip-grating', 'Angle Frame With Non Slip Grating'),
    ('prd-drainage-angle-frame-slotted-top', 'Angle Frame With Slotted Top'),
    ('prd-drainage-channel-grating', 'Channel Grating'),
    ('prd-drainage-channel-heel-guard', 'Channel With Heel Guard'),
    ('prd-drainage-channel-non-slip-grating', 'Channel With Non Slip Grating'),
    ('prd-drainage-heavy-duty-grating', 'Heavy Duty Grating'),
    ('prd-drainage-ladder-type-grating', 'Ladder Type Grating'),
    ('prd-drainage-ss-ladder-grating-frame', 'SS Ladder Type Grating With Frame'),
    ('prd-drainage-industrial-floor-grating', 'Industrial Floor Grating'),
    ('prd-drainage-ss-rain-water-outlet', 'SS Rain Water Outlet'),
    ('prd-drainage-alu-clean-out', 'Aluminium Clean Out'),
    ('prd-drainage-powder-coated-clean-out', 'Powder Coated Clean Out'),
    ('prd-drainage-roof-drain', 'Roof Drain'),
    ('prd-drainage-rain-water-outlet-round', 'Rain Water Outlet - Round'),
    ('prd-drainage-ss-flap-type-drain', 'SS Flap Type Drain'),
    ('prd-drainage-scrupper-drain', 'Scupper Drain'),
    ('prd-drainage-slotted-drain-outlet', 'Slotted Drain Outlet'),
    ('prd-drainage-parapet-drain', 'Parapet Drain'),

    # ---- Tailor Made Products (End To End reference folder) ----
    ('prd-tme-handrail', 'Handrail'),
    ('prd-tme-ss-handrail', 'SS Handrail'),
    ('prd-tme-glass-handrail', 'Glass Handrail'),
    ('prd-tme-handrail-glass-partition', 'Handrail With Glass Partition'),
    ('prd-tme-handrail-wooden-handle', 'Handrail With Wooden Handle'),
    ('prd-tme-staircase-handrail', 'Staircase Handrail'),
    ('prd-tme-wall-mounted-handrail', 'Wall Mounted Handrail'),
    ('prd-tme-pool-handrail', 'Swimming Pool Handrail'),
    ('prd-tme-ladder', 'Ladder'),
    ('prd-tme-sliding-door', 'Sliding Door'),
    ('prd-tme-lift-cladding', 'Lift Cladding'),
    ('prd-tme-wall-fencing', 'Wall Fencing'),
    ('prd-tme-corner-guard', 'Stainless Steel Corner Guard'),
    ('prd-tme-ceiling-tile', 'Ceiling Tile'),
    ('prd-tme-roof-platform', 'Platform For Roof'),
    ('prd-tme-pool-platform', 'Swimming Pool Platform'),
    ('prd-tme-marble-top', 'Marble Top'),
    ('prd-tme-powder-coated-cabinet', 'Powder Coated Cabinet'),
    ('prd-tme-storage-shelving', 'Storage Shelving'),
    ('prd-tme-flower-stand', 'Flower Stand'),
    ('prd-tme-floor-mounting-bollard', 'Floor Mounting Bollard'),
    ('prd-tme-ev-charging-unit', 'EV Charging Unit'),
    ('prd-tme-outdoor-light-box', 'Outdoor Light Box'),
    ('prd-tme-bbq-tray', 'BBQ Tray'),
]

# Tailor Made Products picks up every photo the other five categories didn't
# explicitly claim. Validate as we go so a typo'd slug fails loudly.
_ALL_PHOTO_SLUGS = [s for s, _ in ALL_PRODUCT_PHOTOS]
_CLAIMED = _UPVC_SLUGS + _HATCH_SLUGS + _KITCHEN_SLUGS + _HANDRAIL_SLUGS + _DECORATIVE_SLUGS + _DRAINAGE_SLUGS
for _s in _CLAIMED:
    assert _s in _ALL_PHOTO_SLUGS, f'unknown photo slug in a product category: {_s}'
assert len(_CLAIMED) == len(set(_CLAIMED)), 'a photo slug is claimed by more than one category'
PRODUCT_CATEGORIES[-1]['photos'] = [s for s in _ALL_PHOTO_SLUGS if s not in set(_CLAIMED)]

CLIENTS = ['MBS (Meemar Building System)', 'SEWA', 'Al Ghurair Iron &amp; Steel', 'Lamprel',
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
    ('Value engineering',
     'We design as per your requirements based on site conditions, and apply value engineering principles when estimating costs to optimize both performance and budget.'),
]

FAQ = [
    ('Do you work as a subcontractor to main contractors?',
     'Yes. Most of our reference projects were delivered under main contractors and steel suppliers including MBS (Meemar Building System), Al Aamedah Al Maseyah, Al Aswar Contracting and Capital Engineering Consultant, for end clients such as SEWA, Lamprel, Six Sigma and Al Ghurair Iron &amp; Steel.'),
    ('Which emirates do you cover?',
     'We are licensed in Dubai and Sharjah and have delivered projects in Sharjah, Dubai and Abu Dhabi, including Hamriyah Free Zone, Khalid Port, ICAD-1 Mussafah and Kizad. We mobilise to the Northern Emirates on request.'),
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
    caret = '<svg class="nav__care" viewBox="0 0 10 6" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M1 1l4 4 4-4"/></svg>'

    def desktop_item(n, h):
        if n != 'Services':
            return f'<a class="nav__a" href="{href_for(h)}" data-nav-link>{n}</a>'
        drop = ''.join(f'<a href="{base}services/{s["slug"]}.html">{s["title"]}</a>' for s in SERVICES)
        return f'''<div class="nav__item">
      <a class="nav__a" href="{href_for(h)}" data-nav-link>{n}{caret}</a>
      <div class="nav__drop">{drop}</div>
    </div>'''

    def mobile_item(i, n, h):
        num = f'<span class="mono">{i+1:02d}</span>'
        if n != 'Services':
            return f'<a href="{href_for(h)}" data-nav-link>{num}{n}</a>'
        drop = ''.join(f'<a href="{base}services/{s["slug"]}.html">{s["title"]}</a>' for s in SERVICES)
        return f'''<details class="msub">
        <summary>{num}{n}{caret}</summary>
        <div class="msub__list">{drop}</div>
      </details>'''

    links = ''.join(desktop_item(n, h) for n, h in NAV)
    mlinks = ''.join(mobile_item(i, n, h) for i, (n, h) in enumerate(NAV))
    return f'''
<header class="nav">
  <div class="nav__in">
    <a class="nav__logo brand" href="{base}index.html" aria-label="{CO} home">
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
    prd = ''.join(f'<li><a href="{base}products/{p["slug"]}.html">{p["title"]}</a></li>' for p in PRODUCT_CATEGORIES)
    return f'''
<footer class="ft">
  <div class="wrap">
    <div class="ft__top">
      <div class="ft__brand">
        <span class="ft__logo brand" role="img" aria-label="{CO}">
          <span class="brand__tick" aria-hidden="true"></span>
          <span class="brand__mark">ADSD</span>
        </span>
        <p>Structural steel fabrication, erection and industrial metalwork, plus tailor-made fabrication for the civil, MEP and landscape and hospitality sectors, self-performed across the UAE from Dubai and Sharjah.</p>
      </div>
      <div class="ft__col">
        <h3>Services</h3>
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
      <p>© <span id="yr">2026</span> {CO}. TRN {TRN}</p>
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
                    "@type": "OfferCatalog", "name": "Services",
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
      <a class="pc" href="products/{pc['slug']}.html">
        <div class="pc__m">
          {img_tag(pc['hero'], pc['title'] + ', ' + CO_SHORT, 800, 600)}
          <div class="pc__ov">
            <h3 class="h4 pc__t">{pc['title']}</h3>
            <span class="btn btn--pri btn--sm pc__cta"><span class="btn__t">Explore More</span>{ICON['arrow']}</span>
          </div>
        </div>
      </a>''' for pc in PRODUCT_CATEGORIES)

    proc = ''.join(f'''
      <div class="proc__s">
        <span class="proc__bar" aria-hidden="true"></span>
        <p class="proc__n">Step {i+1:02d}</p>
        <h3>{t}</h3>
        <p>{d}</p>
      </div>''' for i, (t, d) in enumerate(PROCESS))

    proj = ''.join(f'''
      <div class="proj__item">
        <figure class="gal__i proj__m" data-full="assets/img/{g}-1400.jpg">
          <img src="assets/img/{g}-800.jpg" alt="{n}, {loc}" width="800" height="600" loading="lazy" decoding="async">
        </figure>
        <div class="proj__body">
          <h3 class="h4 proj__cap">{n}</h3>
          <p class="proj__loc">{loc}</p>
        </div>
      </div>''' for g, n, loc in PROJECTS)

    QUOTES = [
        ('They fabricate and erect with the same crew, so fit-up problems get solved on the day instead of turning into a fortnight of correspondence.',
         'Project Manager', 'Main contractor, Abu Dhabi'),
        ('Deliveries arrived in the sequence we asked for. That sounds minor until you have a crane on standby waiting for the right rafter.',
         'Site Engineer', 'Industrial project, Sharjah'),
        ('The secondary metalwork (handrails, louvers, chequer plate) was measured on site and fitted first time. It cleared the snag list.',
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

    title = f'{CO} | Structural Steel Fabrication &amp; Erection, Dubai'
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
        <p class="eyebrow eyebrow--i" data-hero-eye>Dubai · Sharjah · Abu Dhabi, licensed since 2022</p>
        <h1 class="h1 hero__h1" data-hero-h>Structural steel, fabricated and erected to the grid line.</h1>
        <p class="lead lead--i hero__sub" data-hero-sub>{CO} fabricates and installs structural steel, industrial metalwork and tailor-made fabrication products for the civil, MEP and landscape and hospitality sectors, self-performed by our own workshop and site crews.</p>
        <div class="hero__acts" data-hero-act>
          <a class="btn btn--pri" href="#contact" data-magnet="0.22"><span class="btn__t">Request a quotation</span>{ICON['arrow']}</a>
          <a class="btn btn--ghost-i" href="#services" data-magnet="0.18"><span class="btn__t">See our services</span></a>
        </div>
      </div>

      <div class="hero__specs" data-hero-spec>
        <div><span class="spec__k">Established</span><span class="spec__v"><span data-count="2022" data-dec="0">2022</span></span></div>
        <div><span class="spec__k">Disciplines</span><span class="spec__v"><span data-count="5">5</span></span></div>
        <div><span class="spec__k">Reference projects</span><span class="spec__v"><span data-count="8">8</span></span></div>
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
          <p data-reveal>{CO} works from two bases: a Sharjah workshop that has held an industrial licence since 2022, and a Dubai contracting licence issued by the Department of Economy and Tourism, fabricating and erecting structural steel, metalwork and tailor-made fabrication products across the Emirates.</p>

          <p data-reveal>We are a diversified metal fabrication company serving the commercial and residential sectors, providing products and systems for structural applications, MEP requirements, landscape installations and hospitality projects. Each project is designed according to your specific requirements and site conditions, with solutions tailored to your needs whether for drainage systems, handrails, screens, or any custom fabrication.</p>

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
          <figcaption class="cap" style="grid-column:1/-1"><b>Fig. 01</b> Workshop: cutting, fitting, welding and finishing before anything reaches site.</figcaption>
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

  <!-- ========================================================= SERVICES -->
  <section class="sec sec--paper" id="services">
    <div class="wrap">
      <div class="shead">
        <div class="shead__top"><span class="shead__idx">03</span><p class="eyebrow">Services</p></div>
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
          <p class="lead" data-reveal>Product categories drawn from completed projects: UPVC drainage, dedicated drainage products, access hatches and covers, customised kitchens, handrails, decorative metalwork, and tailor-made fabrication. Open a category for the full range.</p>
        </div>
      </div>
      <div class="prod" data-stagger>{prod}</div>
      <div class="prod__more" data-reveal>
        <a class="tlink" href="gallery.html">Explore gallery{ICON['arr_sm']}</a>
      </div>
    </div>
  </section>

  <!-- ========================================================= PROCESS -->
  <section class="sec sec--ink" id="process">
    <div class="wrap">
      <div class="shead">
        <div class="shead__top"><span class="shead__idx">05</span><p class="eyebrow eyebrow--i">Process</p></div>
        <div class="shead__grid">
          <h2 class="h2 shead__title" data-split>Enquiry to handover, in five steps.</h2>
          <p class="lead lead--i" data-reveal>The sequence is genuinely sequential: nothing gets cut before drawings are approved, and nothing leaves the workshop out of erection order.</p>
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
          <h2 class="h2 shead__title" data-split>Work we can point to.</h2>
          <p class="lead" data-reveal>Villas, hospitality fit-outs and civil sites across the UAE. Click a photo for a larger view.</p>
        </div>
      </div>
      <div class="proj" data-stagger>{proj}</div>
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
          <p class="lead lead--i" data-reveal>For any kind of building project, feel free to reach our sales staff, who will assist you by phone or email for a free quotation.</p>
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
          <div class="f"><label for="message">Scope description</label><textarea id="message" name="message" rows="4" placeholder="Location, programme dates, tonnage or drawing reference, whatever you have." required></textarea><span class="f__err"></span></div>
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
    bens = ''.join(f'<li>{ICON["tick"]}<span><b>{t}</b>: {d}</span></li>' for t, d in s['benefits'])
    specs = ''.join(f'<div><dt>{k}</dt><dd>{v}</dd></div>' for k, v in s['specs'])
    gal = ''.join(f'''
      <figure class="gal__i" data-full="{base}assets/img/{g}-1400.jpg">
        <img src="{base}assets/img/{g}-800.jpg" alt="{html.unescape(s['plain'])}: {g.replace('-',' ')}" width="800" height="800" loading="lazy" decoding="async">
      </figure>''' for g in s['gallery'])
    body = ''.join(f'<p data-reveal>{p}</p>' for p in s['body'])

    plain = html.unescape(s['plain'])
    title = f'{s["title"]} | {CO_SHORT}, Dubai'
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
            {"@type": "ListItem", "position": 2, "name": "Services", "item": SITE + "/#services"},
            {"@type": "ListItem", "position": 3, "name": plain, "item": canon}]}]}

    return head(title, desc, canon, base, jsonld=ld) + shell_open(base) + nav(base) + f'''
<main id="main">

  <section class="phero">
    <div class="phero__bg" aria-hidden="true">
      <img src="{base}assets/img/{s['hero']}-1400.jpg" alt="" width="1400" height="1400" fetchpriority="high" decoding="async" data-parallax="-8">
    </div>
    <div class="wrap phero__in">
      <nav class="crumbs" aria-label="Breadcrumb">
        <a href="{base}index.html">Home</a><span>/</span><a href="{base}index.html#services">Services</a><span>/</span><span style="opacity:1;color:var(--t2i)">{s['title']}</span>
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
          <p class="lead" data-reveal>Six things we do as standard on this discipline, not optional extras priced later.</p>
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
        <a class="tlink" href="{base}index.html#services">All five disciplines{ICON['arr_sm']}</a>
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
    bens = ''.join(f'<li>{ICON["tick"]}<span><b>{t}</b>: {d}</span></li>' for t, d in p['benefits'])
    gal = ''.join(f'''
      <figure class="gal__i{' gal__i--w' if n == 0 else ''}" data-full="{base}assets/img/{g}-1400.jpg">
        <img src="{base}assets/img/{g}-800.jpg" alt="{html.unescape(p['title'])}: {g.replace('-',' ')}" width="800" height="800" loading="lazy" decoding="async">
      </figure>''' for n, g in enumerate(p['gallery']))
    over = ''.join(f'<p data-reveal>{x}</p>' for x in p['overview'])

    plain = html.unescape(p['title'])
    title = f'{p["title"]} | {CO_SHORT}, Dubai'
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
      <p class="eyebrow eyebrow--i" style="margin-top:1.4rem">{p['tag']}, product {i+1:02d} of {len(PRODUCTS)}</p>
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


# =================================================== PRODUCT CATEGORY =====
_PHOTO_TITLE = {s: t for s, t in ALL_PRODUCT_PHOTOS}


def build_product_category(pc, i):
    base = '../'
    others = [x for x in PRODUCT_CATEGORIES if x['slug'] != pc['slug']][:4]
    rel = ''.join(f'<a href="{o["slug"]}.html">{o["title"]}{ICON["arr_sm"]}</a>' for o in others)
    feats = ''.join(f'''
      <article class="card">
        <p class="card__n">{n+1:02d}</p>
        <h3 class="h4">{t}</h3>
        <p>{d}</p>
      </article>''' for n, (t, d) in enumerate(pc['features']))
    specs = ''.join(f'<div><dt>{k}</dt><dd>{v}</dd></div>' for k, v in pc['specs'])
    bens = ''.join(f'<li>{ICON["tick"]}<span><b>{t}</b>: {d}</span></li>' for t, d in pc['benefits'])
    pgrid = ''.join(f'''
      <div class="pgrid__item">
        <figure class="gal__i" data-full="{base}assets/img/{g}-1400.jpg">
          <img src="{base}assets/img/{g}-800.jpg" alt="{_PHOTO_TITLE[g]}" width="800" height="800" loading="lazy" decoding="async">
        </figure>
        <p class="pgrid__cap">{_PHOTO_TITLE[g]}</p>
      </div>''' for g in pc['photos'])
    over = ''.join(f'<p data-reveal>{x}</p>' for x in pc['overview'])

    plain = html.unescape(pc['title'])
    title = f'{pc["title"]} | {CO_SHORT}, Dubai'
    desc = html.unescape(pc['short'])
    canon = f'{SITE}/products/{pc["slug"]}.html'
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "CollectionPage", "name": plain, "url": canon, "description": desc,
         "mainEntity": {"@type": "ItemList", "numberOfItems": len(pc['photos'])}},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Products", "item": SITE + "/#products"},
            {"@type": "ListItem", "position": 3, "name": plain, "item": canon}]}]}

    return head(title, desc, canon, base, jsonld=ld) + shell_open(base) + nav(base) + f'''
<main id="main">

  <section class="phero">
    <div class="phero__bg" aria-hidden="true">
      <img src="{base}assets/img/{pc['hero']}-1400.jpg" alt="" width="1400" height="1400" fetchpriority="high" decoding="async" data-parallax="-8">
    </div>
    <div class="wrap phero__in">
      <nav class="crumbs" aria-label="Breadcrumb">
        <a href="{base}index.html">Home</a><span>/</span><a href="{base}index.html#products">Products</a><span>/</span><span style="opacity:1;color:var(--t2i)">{pc['title']}</span>
      </nav>
      <p class="eyebrow eyebrow--i" style="margin-top:1.4rem">{pc['tag']}, category {i+1:02d} of {len(PRODUCT_CATEGORIES)}</p>
      <h1 class="h1 phero__h" data-hero-h>{pc['title']}</h1>
      <p class="lead lead--i phero__d" data-hero-sub>{pc['lead']}</p>
      <div class="hero__acts" data-hero-act>
        <a class="btn btn--pri" href="{base}index.html#contact" data-magnet="0.22"><span class="btn__t">Request a quotation</span>{ICON['arrow']}</a>
        <a class="btn btn--ghost-i" href="mailto:{EMAIL}" data-magnet="0.18"><span class="btn__t">{EMAIL}</span></a>
      </div>
    </div>
  </section>

  <section class="sec sec--paper">
    <div class="wrap two">
      <div class="rich">
        <p class="eyebrow" data-reveal>Overview</p>
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
          <p class="lead" data-reveal>Six things included in every {pc['noun']} package we supply.</p>
        </div>
      </div>
      <div class="cards cards--3" data-stagger>{feats}</div>
    </div>
  </section>

  <section class="sec sec--paper">
    <div class="wrap">
      <div class="dim" style="margin-bottom:1.6rem">
        <span class="dim__txt">Gallery</span><span class="dim__line"></span><span class="dim__txt">{len(pc['photos'])} photographs</span>
      </div>
      <div class="pgrid" data-stagger>{pgrid}</div>
    </div>
  </section>

  <section class="sec sec--white">
    <div class="wrap two">
      <div>
        <p class="eyebrow" data-reveal>Related categories</p>
        <h2 class="h2" style="margin-top:1rem;max-width:22ch" data-split>Looking for something else?</h2>
      </div>
      <div class="aside" style="position:static" data-reveal>
        <div class="aside__list">{rel}</div>
        <a class="tlink" href="{base}index.html#products">All {len(PRODUCT_CATEGORIES)} categories{ICON['arr_sm']}</a>
      </div>
    </div>
  </section>

</main>
{cta(base, pc['photos'][1] if len(pc['photos']) > 1 else pc['hero'],
     'Enquire', 'Tell us what you need. We will price the ' + pc['noun'] + ' work.',
     'Send drawings, a site photo, or a description of what you need. Quotations are free.')}
{footer(base)}'''


def build_gallery():
    gal = ''.join(f'''
      <figure class="gal__i{' gal__i--w' if i in (0, 9) else ''}" data-full="assets/img/{g}-1400.jpg">
        <img src="assets/img/{g}-800.jpg" alt="{a}" width="800" height="800" loading="lazy" decoding="async">
      </figure>''' for i, (g, a) in enumerate(GALLERY))

    title = f'Project Gallery | {CO_SHORT}, Dubai'
    desc = 'Fabrication and installation photography from ADSD Steel reference projects: structural steel, handrails and balustrades, access covers, cladding and bespoke metalwork.'
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
      <p class="lead lead--i phero__d" data-hero-sub>Structural steel, handrails and balustrades, access covers, cladding and bespoke metalwork, own fabrication and site work, drawn from our reference projects.</p>
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
    </div>
  </section>

</main>
{cta('', 'ssf-canopy-entrance', 'Enquire',
     'Send drawings. Get a priced take-off.',
     'Quotations are free. Give us the location, the programme dates and whatever drawings you have.')}
{footer()}'''


# ========================================================= ALL PRODUCTS =====
ALLPROD_OVERVIEW = [
    'This page is a working photograph library rather than a single specified product: access hatches and covers, drains and gratings, handrails and balustrades, kitchen and catering metalwork, enclosures, cabinets and other bespoke items we have fabricated and installed on completed projects across the UAE.',
    'Every item shown was measured, fabricated and fitted to the opening or run it was made for, not picked from a standard catalogue. Treat the photographs as a reference for the kind of work we take on. Send us a drawing, a site photo, or a description of what you need, and we will confirm size, material and finish before quoting.',
]
ALLPROD_BENEFITS = [
    ('Made to the actual opening', 'Every item is measured on site or against your drawing, not selected from a standard size run.'),
    ('One crew, start to finish', 'The same team fabricates and installs, so a hatch, drain or handrail arrives fitted rather than boxed and left for someone else.'),
    ('Small works handled properly', 'Single items and short runs get the same shop-drawing and finish control as a full package.'),
    ('Matched to the rest of the works', 'Where these items sit inside a larger scope, they are detailed to suit the structural steel or metalwork already being fabricated for the same project.'),
]
ALLPROD_SPECS = [
    ('Categories shown', 'Access hatches and covers, drains and gratings, handrails and balustrades, kitchen and catering metalwork, enclosures, cabinets and bespoke fabrication'),
    ('Materials', 'Mild steel, stainless steel, aluminium and GRP, finished to the specified coating or grade'),
    ('Basis', 'Site-measured or drawing-based fabrication, supplied and installed or supply-only'),
    ('Sourcing', 'Photographed on completed projects, not stock imagery'),
    ('Quotation', 'Free, based on your drawing, a site measurement, or a reference photo from this page'),
]
ALLPROD_FEATURES = [
    ('Access hatches and covers', 'Floor, roof and wall access hatches and panels, sized to the opening and finished to suit the surrounding surface.'),
    ('Drains and gratings', 'Floor gullies, linear slot drains, pool and ablution gratings, and manhole and trench covers.'),
    ('Handrails and balustrades', 'Stair, ramp and balcony handrails in tube, box section, glass-infill and stainless steel.'),
    ('Kitchen and catering metalwork', 'Extraction hoods and ducting, worktops, sinks, trolleys and storage units for commercial kitchens.'),
    ('Enclosures and cabinets', 'Plant enclosures, meter boxes, staff lockers and storage cabinets fabricated to the space available.'),
    ('Bespoke and decorative items', 'Screens, display units, planters and one-off fabrication built to a design rather than a standard part.'),
]


def build_all_products():
    pgrid = ''.join(f'''
      <div class="pgrid__item">
        <figure class="gal__i" data-full="assets/img/{g}-1400.jpg">
          <img src="assets/img/{g}-800.jpg" alt="{t}" width="800" height="800" loading="lazy" decoding="async">
        </figure>
        <p class="pgrid__cap">{t}</p>
      </div>''' for g, t in ALL_PRODUCT_PHOTOS)

    over = ''.join(f'<p data-reveal>{x}</p>' for x in ALLPROD_OVERVIEW)
    bens = ''.join(f'<li>{ICON["tick"]}<span><b>{t}</b>: {d}</span></li>' for t, d in ALLPROD_BENEFITS)
    specs = ''.join(f'<div><dt>{k}</dt><dd>{v}</dd></div>' for k, v in ALLPROD_SPECS)
    feats = ''.join(f'''
      <article class="card">
        <p class="card__n">{n+1:02d}</p>
        <h3 class="h4">{t}</h3>
        <p>{d}</p>
      </article>''' for n, (t, d) in enumerate(ALLPROD_FEATURES))

    title = f'All Products | {CO_SHORT}, Dubai'
    desc = ('The full range of products fabricated and installed by ' + CO + ': access hatches and covers, '
            'handrails, drains, kitchen and catering metalwork, enclosures and bespoke items, drawn from '
            'completed projects.')
    canon = f'{SITE}/all-products.html'
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "ImageGallery", "name": "ADSD Steel: All Products", "url": canon, "description": desc},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": "All Products", "item": canon}]}]}

    return head(title, desc, canon, jsonld=ld) + shell_open() + nav() + f'''
<main id="main">

  <section class="phero">
    <div class="phero__bg" aria-hidden="true">
      <img src="assets/img/prd-access-hatch-1-1400.jpg" alt="" width="1400" height="1400" fetchpriority="high" decoding="async" data-parallax="-8">
    </div>
    <div class="wrap phero__in">
      <nav class="crumbs" aria-label="Breadcrumb">
        <a href="index.html">Home</a><span>/</span><span style="opacity:1;color:var(--t2i)">All Products</span>
      </nav>
      <p class="eyebrow eyebrow--i" style="margin-top:1.4rem">Products</p>
      <h1 class="h1 phero__h" data-hero-h>Every product, one page.</h1>
      <p class="lead lead--i phero__d" data-hero-sub>Access hatches and covers, drains, handrails, kitchen and catering metalwork, enclosures and bespoke items, photographed on completed projects. Click any photo for a larger view.</p>
      <div class="hero__acts" data-hero-act>
        <a class="btn btn--pri" href="index.html#contact" data-magnet="0.22"><span class="btn__t">Request a quotation</span>{ICON['arrow']}</a>
        <a class="btn btn--ghost-i" href="tel:{PHONE_H}" data-magnet="0.18"><span class="btn__t">{PHONE}</span></a>
      </div>
    </div>
  </section>

  <section class="sec sec--paper">
    <div class="wrap two">
      <div class="rich">
        <p class="eyebrow" data-reveal>Overview</p>
        {over}
        <h2 class="h3" style="margin-top:1.4rem" data-reveal>Benefits</h2>
        <ul class="ticks" data-stagger>{bens}</ul>
      </div>
      <aside class="aside" data-reveal>
        <h3 class="h4">Scope and specification</h3>
        <dl class="specs-tbl">{specs}</dl>
        <a class="tlink" href="index.html#contact">Enquire about an item{ICON['arr_sm']}</a>
      </aside>
    </div>
  </section>

  <section class="sec sec--white">
    <div class="wrap">
      <div class="shead">
        <div class="shead__top"><span class="shead__idx">01</span><p class="eyebrow">Key features</p></div>
        <div class="shead__grid">
          <h2 class="h2 shead__title" data-split>What the photographs cover.</h2>
          <p class="lead" data-reveal>The 106 photographs below fall into six groups, a sample of the small works we take on alongside the main scope.</p>
        </div>
      </div>
      <div class="cards cards--3" data-stagger>{feats}</div>
    </div>
  </section>

  <section class="sec sec--paper">
    <div class="wrap">
      <div class="dim" style="margin-bottom:1.6rem">
        <span class="dim__txt">Gallery</span><span class="dim__line"></span><span class="dim__txt">{len(ALL_PRODUCT_PHOTOS)} items</span>
      </div>
      <div class="pgrid" data-stagger>{pgrid}</div>
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
write('all-products.html', build_all_products())
for i, s in enumerate(SERVICES):
    write(f'services/{s["slug"]}.html', build_service(s, i))
for i, p in enumerate(PRODUCTS):
    write(f'products/{p["slug"]}.html', build_product(p, i))
for i, pc in enumerate(PRODUCT_CATEGORIES):
    write(f'products/{pc["slug"]}.html', build_product_category(pc, i))

# sitemap + robots
urls = [(SITE + '/', '1.0'), (SITE + '/gallery.html', '0.6'), (SITE + '/all-products.html', '0.6')]
urls += [(f'{SITE}/services/{s["slug"]}.html', '0.8') for s in SERVICES]
urls += [(f'{SITE}/products/{p["slug"]}.html', '0.8') for p in PRODUCTS]
urls += [(f'{SITE}/products/{pc["slug"]}.html', '0.8') for pc in PRODUCT_CATEGORIES]
write('sitemap.xml', '<?xml version="1.0" encoding="UTF-8"?>\n'
      '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
      + ''.join(f'  <url><loc>{u}</loc><priority>{p}</priority></url>\n' for u, p in urls)
      + '</urlset>\n')
write('robots.txt', f'User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n')

print(f'built 2 + {len(SERVICES)} + {len(PRODUCTS)} + {len(PRODUCT_CATEGORIES)} = '
      f'{2+len(SERVICES)+len(PRODUCTS)+len(PRODUCT_CATEGORIES)} pages')
