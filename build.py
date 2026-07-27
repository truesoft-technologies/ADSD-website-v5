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
EMAIL   = 'ads.techdxb@gmail.com'
POBOX   = 'P.O. Box 282615, Dubai, UAE'
TRN     = '104023207400003'
LIC_DXB = '1050680'
LIC_SHJ = '502971'

NAV = [
    ('About',      '#about'),
    ('Capability', '#capability'),
    ('Products',   '#products'),
    ('Industries', '#industries'),
    ('Projects',   '#projects'),
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
        gallery=['fabricated-beams', 'frame-erection-crane', 'curved-roof-erection', 'warehouse-frame-erected',
                 'portal-frame-lift', 'portal-structure-glazed'],
    ),
    dict(
        slug='equipment-installation',
        title='Equipment Installation',
        plain='Equipment Installation',
        short='Setting, aligning and grouting production plant, conveyors, silos and packaged units on prepared foundations.',
        hero='silo-platform-access',
        lead='Mechanical installation of production plant and packaged equipment — rigged into place, aligned to tolerance, grouted and handed to your commissioning team.',
        body=[
            'Equipment installation is where a plant layout stops being a drawing. We take delivery of the unit, check the foundation and holding-down bolts against the vendor drawing, rig the equipment into position, then shim, align and grout it to the tolerances the manufacturer specifies.',
            'Most installations also need steel that was never on the equipment order: access platforms, maintenance walkways, hopper supports, guarding and small bracketry. Because we fabricate as well as install, that steel is made and fitted by the same team instead of becoming a separate package with its own lead time.',
        ],
        features=[
            ('Foundation and bolt check', 'Anchor positions, projections and levels verified against the vendor drawing before the unit is lifted.'),
            ('Rigging and placement', 'Lift plans, slinging and setting of skids, tanks, conveyors, silos and packaged units into final position.'),
            ('Alignment and grouting', 'Shimming, levelling and laser or dial alignment, then non-shrink grouting of base plates and soleplates.'),
            ('Support and access steel', 'Platforms, stairs, walkways, hopper supports and guarding fabricated to suit the equipment as installed.'),
            ('Mechanical connection', 'Coupling of guards, chutes, ducts and inline items ready for the electrical and instrument trades.'),
            ('Handover for commissioning', 'Alignment records, torque records and a walkdown with your commissioning engineer.'),
        ],
        benefits=[
            ('Vendor tolerances met', 'Alignment is recorded, not assumed, so warranty conditions on rotating plant are protected.'),
            ('No gap between disciplines', 'Access steel, guarding and brackets come from the same team, closing the usual gap between supply and install.'),
            ('Works around production', 'Installations are sequenced for shutdown windows and night work where a plant cannot stop.'),
            ('Site-ready crews', 'Riggers, fitters and welders arrive with the certification and PPE your site induction requires.'),
        ],
        specs=[
            ('Equipment types', 'Process skids, conveyors, silos, hoppers, mixers, pumps, packaged plant'),
            ('Alignment methods', 'Precision level, dial gauge and laser alignment as the vendor specification requires'),
            ('Grouting', 'Cementitious and epoxy non-shrink grouts to the specified bearing area'),
            ('Rigging', 'Method statements and lift plans issued for approval before mobilisation'),
            ('Interfaces', 'Coordinated with civil, electrical and instrumentation contractors'),
            ('Working hours', 'Day shift, night shift and shutdown working available'),
        ],
        gallery=['plant-steel-structure', 'process-platform-steel', 'workshop-interior-crane', 'tank-platform-crane',
                 'portal-frame-crane'],
    ),
    dict(
        slug='pipe-fabrication',
        title='Pipe Fabrication, Installation &amp; Inline Equipment',
        plain='Pipe Fabrication, Installation and Inline Equipment',
        short='Shop and field spooling in carbon and stainless steel, with valves, strainers and inline items set to the P&amp;ID.',
        hero='plant-steel-structure',
        lead='Pipe spools fabricated to the isometric, installed on pipe supports we make ourselves, with valves and inline equipment set the right way round.',
        body=[
            'Pipework is fabricated from the isometrics as spools wherever shop conditions will give a better weld than a site position would. Spools are marked, tacked, welded and dimensionally checked before they leave the workshop, then installed against the line list and P&amp;ID.',
            'Inline equipment — valves, strainers, flow elements, sight glasses — is fitted with attention to orientation, flow direction and access for operation and maintenance. Pipe supports, shoes, guides and small structural steel are made in the same workshop, so a support that does not suit the route can be modified the same day.',
        ],
        features=[
            ('Spool fabrication', 'Cutting, bevelling, fit-up and welding of carbon and stainless spools from approved isometrics.'),
            ('Field erection', 'Routing, hanging and closure welds against the line list, P&amp;ID and approved route drawings.'),
            ('Inline equipment', 'Valves, strainers, flow elements and instrument connections installed to orientation and flow direction.'),
            ('Pipe supports', 'Shoes, guides, anchors, hangers and support steel fabricated in-house to suit the installed route.'),
            ('Test support', 'Preparation for hydrostatic and pneumatic testing, including temporary spades, vents and drains.'),
            ('Reinstatement', 'Painting, insulation interface and clean handover of the completed line.'),
        ],
        benefits=[
            ('Better welds, fewer positions', 'Shop-welded spools reduce overhead and confined-position welding on site.'),
            ('Supports made to fit', 'Support steel is fabricated against the installed route, not just the design assumption.'),
            ('Maintainable layouts', 'Valve handles, strainer baskets and instrument taps are set where an operator can actually reach them.'),
            ('Single interface', 'Pipe, supports and structural steel come from one supplier with one programme.'),
        ],
        specs=[
            ('Materials', 'Carbon steel, stainless steel, galvanised pipework'),
            ('Joining', 'Butt-welded, socket-welded, flanged and threaded connections'),
            ('Fabrication basis', 'Approved isometrics, line lists and P&amp;IDs'),
            ('Inline items', 'Valves, strainers, sight glasses, flow elements, instrument connections'),
            ('Testing', 'Hydrostatic and pneumatic test support with your QA/QC team'),
            ('Supports', 'Shoes, guides, anchors, spring hangers, fabricated support steel'),
        ],
        gallery=['tank-installation-plant', 'process-platform-steel', 'silo-platform-access', 'plant-steel-structure'],
    ),
    dict(
        slug='tank-installation',
        title='Tank Installation',
        plain='Tanks Installation',
        short='Shell erection, internals and access steel for storage and process tanks, complete with testing support.',
        hero='tank-installation-plant',
        lead='Storage and process tanks set, erected and fitted out — shell, internals, nozzles and the access steel that makes them serviceable.',
        body=[
            'Tank work covers both the placing of shop-built vessels and the site erection of plate tanks. Foundations and anchor arrangements are checked first, then the tank is rigged into position, plumbed and secured, with shell courses, roof plates and nozzles set out to the fabrication drawing.',
            'A tank is only useful if it can be operated and inspected, so the scope normally extends to platforms, cage ladders, handrails, dip hatches, gauge access and pipe supports. All of that steel is fabricated in our own workshop against the tank as installed rather than against an assumed dimension.',
        ],
        features=[
            ('Foundation verification', 'Levels, anchor bolt positions and bearing arrangement checked before placement.'),
            ('Placement and erection', 'Rigging of shop-built vessels, or site erection of shell courses, annular plates and roof.'),
            ('Nozzles and internals', 'Nozzle setting, manway fit-up, baffles, supports and internal steel to the fabrication drawing.'),
            ('Access steel', 'Platforms, cage ladders, stairs and handrails to give safe operating and inspection access.'),
            ('Testing support', 'Preparation and attendance for hydrostatic and leak testing with your inspection team.'),
            ('Coating and insulation interface', 'Surface preparation, primer and finish, and coordination with the insulation contractor.'),
        ],
        benefits=[
            ('Access designed in', 'Platforms and ladders are fabricated to the installed tank, so gauges and manways are genuinely reachable.'),
            ('One team, shell to handrail', 'Vessel work and secondary steel are not split between two contractors with two programmes.'),
            ('Inspection-ready', 'Weld records, alignment checks and test preparation are handled as part of the scope.'),
            ('Site-condition experience', 'Work delivered inside live industrial plants across the UAE, including phased shutdowns.'),
        ],
        specs=[
            ('Tank types', 'Vertical and horizontal storage tanks, process vessels, day tanks, buffer tanks'),
            ('Scope', 'Placement of shop-built vessels or site erection of plate tanks'),
            ('Fittings', 'Nozzles, manways, dip hatches, vents, level and gauge connections'),
            ('Access', 'Platforms, cage ladders, stairs, handrails, chequer plate walkways'),
            ('Testing', 'Hydrostatic and leak test support'),
            ('Finish', 'Specified primer and finish system, insulation interface coordinated'),
        ],
        gallery=['tank-installation-plant', 'silo-platform-access', 'process-platform-steel', 'tank-platform-crane'],
    ),
    dict(
        slug='miscellaneous-metal-works',
        title='Miscellaneous Metal Works',
        plain='Miscellaneous Metal Work',
        short='Handrails, ladders, aluminium louvers, car parking sheds and substation chequer plate — the finishing steel.',
        hero='louver-screen-enclosure',
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
        gallery=['louver-screen-corner', 'car-parking-shade-row', 'car-parking-shade-single', 'process-platform-steel'],
    ),
    dict(
        slug='manpower-supply',
        title='Manpower Supply',
        plain='Manpower supply',
        short='Trade-tested fabricators, welders, riggers, fitters and helpers released to your site under your supervision.',
        hero='fabrication-welding',
        lead='Trade-tested steel and mechanical labour released to your project — by the day, the month or the duration of the contract.',
        body=[
            'When your own programme is tighter than your own crew, we release trades from the same workforce that staffs our contracts. Welders, fabricators, fitters, riggers, painters and helpers are available with the trade test, experience and documentation your site induction asks for.',
            'Labour can work under your supervision, or under one of our chargehands if you would rather take an output than manage a crew. Rates, shift patterns, accommodation and transport are agreed in writing before mobilisation so there are no surprises when the invoice arrives.',
        ],
        features=[
            ('Trades available', 'Structural welders, pipe welders, fabricators, fitters, riggers, scaffolders, painters, helpers.'),
            ('Trade-tested', 'Welders and fabricators tested before release, with records provided to your QA/QC team.'),
            ('Documentation ready', 'Valid visas, medicals, insurance and site-safety cards in place for induction.'),
            ('Supervision optional', 'Work under your supervision, or under our chargehand where you want an output rather than a crew.'),
            ('Flexible duration', 'Daily, monthly and contract-duration releases, with agreed shift and overtime patterns.'),
            ('Logistics handled', 'Accommodation, transport and PPE arranged so the crew arrives ready to work.'),
        ],
        benefits=[
            ('Cover a peak without hiring', 'Scale up for an erection window and release the labour when the peak passes.'),
            ('Trades that have done the work', 'The same people who staff our own steel and piping contracts, not agency generalists.'),
            ('Induction without delay', 'Documentation is prepared before mobilisation, so day one is a working day.'),
            ('Costs agreed up front', 'Rates, shifts and overtime are fixed in writing before the crew moves.'),
        ],
        specs=[
            ('Trades', 'Welders (structural and pipe), fabricators, fitters, riggers, painters, scaffolders, helpers'),
            ('Testing', 'Trade tests carried out before release; records issued on request'),
            ('Supervision', 'Client-supervised or ADSD chargehand-supervised'),
            ('Duration', 'Daily, monthly, or contract duration'),
            ('Shifts', 'Day, night and rotating shift patterns'),
            ('Provided', 'PPE, transport and accommodation as agreed in the release terms'),
        ],
        gallery=['steel-cutting', 'workshop-interior-crane', 'fabricated-beams', 'structure-under-erection'],
    ),
    dict(
        slug='anchor-bolts-fasteners-supply',
        title='Anchor Bolts &amp; Fastener Supply',
        plain='Anchor Bolts and Fasteners Supply',
        short='Holding-down bolt assemblies, templates and structural fasteners supplied to grade, coating and cast-in schedule.',
        hero='base-plates-fabrication',
        lead='Holding-down bolt assemblies, setting templates and structural fasteners supplied against the base-plate schedule — before the concrete pour, not after it.',
        body=[
            'Anchor bolts are the first steel item on a project and the one most likely to delay it. We supply holding-down bolt assemblies made up to the base-plate detail: bolt, plate washer, nuts, sleeve and the setting template that keeps the group square while the concrete goes in.',
            'Structural bolting for the frame is supplied against the same take-off used for fabrication, so grades, lengths and quantities match the connection details rather than a rounded estimate. Coatings are specified for the exposure the fixing will actually see.',
        ],
        features=[
            ('Holding-down assemblies', 'Bolt, nuts, plate washer, sleeve and cone assembled to the base-plate detail.'),
            ('Setting templates', 'Fabricated templates that hold the bolt group to position and projection through the pour.'),
            ('Structural bolting', 'Bolts, nuts and washers to grade, supplied against the connection schedule.'),
            ('Chemical and mechanical anchors', 'Post-installed anchors where the fixing has to go into cured concrete.'),
            ('Coatings', 'Hot-dip galvanised, zinc plated or self-colour to suit the exposure.'),
            ('Cast-in scheduling', 'Delivered in pour sequence and marked to the grid reference on the drawing.'),
        ],
        benefits=[
            ('The frame fits the bolts', 'Assemblies are made to the base-plate detail, so column bases land on bolts that are where they should be.'),
            ('Pours are not held up', 'Templates and assemblies arrive scheduled against the pour, not against the fabrication programme.'),
            ('Correct grades supplied', 'Quantities and grades come from the same take-off as the steel, so nothing is substituted on site.'),
            ('Right coating, right place', 'External, buried and internal fixings are specified separately rather than uniformly.'),
        ],
        specs=[
            ('Assemblies', 'Holding-down bolts with nuts, plate washers, sleeves and cones'),
            ('Templates', 'Fabricated steel setting templates to bolt-group geometry'),
            ('Structural fasteners', 'Bolts, nuts and washers to specified structural grade'),
            ('Post-installed anchors', 'Chemical and mechanical anchors to approved manufacturer systems'),
            ('Coatings', 'Hot-dip galvanised, zinc plated, self-colour'),
            ('Delivery', 'Marked and batched to grid reference and pour sequence'),
        ],
        gallery=['base-plates-fabrication', 'fabricated-beams', 'warehouse-frame-erected', 'structure-crane-lift'],
    ),
    dict(
        slug='supply-service',
        title='Supply Service',
        plain='Supply Service',
        short='Pre-fabricated building products supplied through our own engineering, manufacturing and delivery systems.',
        hero='supply-team',
        lead='Supply of pre-fabricated construction products, backed by our own engineering, manufacturing and delivery systems — and a sales team you can reach for a free quotation.',
        body=[
            'The company profile commits to supplying exceptional quality products and services in the pre-fabricated construction industry by developing and employing the most advanced information, engineering, manufacturing and delivery systems available. In practice that means a supply route where the drawing, the workshop and the delivery schedule are managed together rather than handed between three parties.',
            'For any kind of building project our sales staff will take the enquiry by phone or email and come back with a free quotation. Where a specification is still open, we will price the options rather than guess which one you meant.',
        ],
        features=[
            ('Pre-fabricated building products', 'Frames, sheds, canopies, cladding, louvers and secondary steel supplied as a package.'),
            ('Engineering support', 'Shop drawings, take-off and material scheduling from your design or performance specification.'),
            ('Manufacturing capacity', 'Own workshop for cutting, drilling, welding and finishing, with capacity reserved against the delivery date.'),
            ('Delivery scheduling', 'Loads planned in the sequence the site needs, with call-off arranged against your programme.'),
            ('Free quotation', 'Enquiries answered by phone or email, with a priced quotation and options where the specification is open.'),
            ('Supply-only or supply and fix', 'Take the material and fix it yourself, or hand the whole scope to our erection crews.'),
        ],
        benefits=[
            ('One quotation, one programme', 'Engineering, manufacture and delivery priced together instead of assembled from three suppliers.'),
            ('Options priced, not assumed', 'Where the specification leaves a choice, you see the cost of each route before deciding.'),
            ('Capacity you can rely on', 'Workshop time is reserved against your delivery date rather than allocated on arrival.'),
            ('A sales team that answers', 'Enquiries handled by named staff, contactable by phone and email.'),
        ],
        specs=[
            ('Product range', 'Pre-engineered frames, sheds, canopies, cladding and roofing, louvers, secondary steel'),
            ('Engineering', 'Shop drawings, take-off, material scheduling'),
            ('Basis of supply', 'Supply only, or supply and fix'),
            ('Quotation', 'Free quotation by phone or email'),
            ('Delivery', 'Scheduled call-off in site sequence'),
            ('Coverage', 'UAE-wide delivery from Dubai and Sharjah'),
        ],
        gallery=['warehouse-exterior', 'open-shed-structure', 'cladding-panel-wall', 'clad-warehouse-green'],
    ),
    dict(
        slug='building-maintenance',
        title='Building Maintenance',
        plain='Building Maintenace',
        short='In-house cleaning, handyman and facility upkeep delivered by our own directly employed and supervised teams.',
        hero='building-maintenance',
        lead='Cleaning, handyman work and facility upkeep carried out by our own directly employed staff — no outsourcing, no subcontracting, one accountable party.',
        body=[
            'Our in-house staff perform all cleaning and maintenance, waste and recycling management, and handyman work, while our trained property managers schedule and monitor everything we do. We are always fully accountable for these services, because our own team carries out the work without outsourcing or subcontracting.',
            'That structure is the point of the service. When a task is missed, there is no chain of suppliers to work through — the manager who set the schedule is the manager who fixes it. Scopes are agreed as a written schedule with frequencies and standards, so performance can be measured rather than debated.',
        ],
        features=[
            ('Cleaning and housekeeping', 'Scheduled cleaning of common areas, offices, industrial floors and external areas.'),
            ('Waste and recycling', 'Waste and recycling management, including segregation and scheduled removal.'),
            ('Handyman work', 'Minor repairs, fixings, doors, fittings and general upkeep across the property.'),
            ('Managed scheduling', 'Trained property managers set, monitor and record the schedule for every task.'),
            ('Directly employed teams', 'All work carried out by our own staff, without outsourcing or subcontracting.'),
            ('Reactive attendance', 'Call-out response for faults and incidents alongside the planned schedule.'),
        ],
        benefits=[
            ('Accountability sits in one place', 'Because nothing is subcontracted, there is one company answering for the standard of the work.'),
            ('Consistent teams on site', 'The same staff attend the property, so they know the building rather than learning it each visit.'),
            ('Measurable performance', 'Frequencies and standards are written down, monitored and reported.'),
            ('Steel and fabric together', 'Structural repairs, handrails and metalwork are handled by the same company that maintains the building.'),
        ],
        specs=[
            ('Cleaning', 'Common areas, offices, industrial floors, external areas, periodic deep cleaning'),
            ('Waste', 'Waste and recycling management with scheduled removal'),
            ('Handyman', 'Minor repairs, fixings, doors, fittings, general upkeep'),
            ('Management', 'Trained property managers scheduling and monitoring all work'),
            ('Delivery model', 'Directly employed teams — no outsourcing or subcontracting'),
            ('Coverage', 'Industrial, commercial and mixed-use properties across Dubai and Sharjah'),
        ],
        gallery=['building-maintenance', 'warehouse-interior-lighting', 'completed-warehouse', 'cladding-blue-facade'],
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
        hero='process-platform-steel',
        lead='Edge protection and access metalwork — stair handrails, platform balustrades, cage ladders and step-overs, fabricated to a site measurement so they fit first time.',
        overview=[
            'Handrails and ladders are safety items, and they are also the last thing installed before an inspection. Both facts argue for measuring the actual structure rather than scaling the drawing: slab edges move, stair rises get adjusted, and a rail fabricated to the design dimension often arrives 30 mm short.',
            'We measure on site, fabricate to that dimension, and install with the fixings the substrate actually needs. Systems are available in galvanised tube, painted section, stainless steel and aluminium, with mid-rails, kick plates and infill panels to suit the exposure and the specification.',
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
        gallery=['process-platform-steel', 'silo-platform-access', 'plant-steel-structure', 'canopy-steel-frame',
                 'workshop-interior-crane', 'tank-platform-crane'],
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
        gallery=['silo-platform-access', 'process-platform-steel', 'plant-steel-structure', 'base-plates-fabrication',
                 'workshop-interior-crane', 'tank-installation-plant'],
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
        gallery=['cladding-blue-facade', 'cladding-panel-wall', 'clad-warehouse-green', 'completed-warehouse',
                 'site-warehouse-build', 'warehouse-exterior'],
    ),
]

# ---------------------------------------------------------------- projects --
PROJECTS = [
    (1,  'Hamriyah Free Zone', 'Sharjah',            'MBS — Meemar Building System', 'SEWA',                     'Completed'),
    (2,  'Ind-18',             'Sharjah',            'Al Aswar Cont. LLC',           '—',                        'Completed'),
    (3,  'Khalid Port',        'Sharjah',            'Al Aamedah Al Maseyah',        'Lamprel',                  'Completed'),
    (4,  'CMW',                'Abu Dhabi',          'MBS — Meemar Building System', 'Six Sigma',                'Completed'),
    (5,  'Hamriyah Free Zone', 'Sharjah',            'Al Aamedah Al Maseyah',        'Lamprel',                  'Completed'),
    (6,  'ICAD-1',             'Mussafah, Abu Dhabi','MBS — Meemar Building System', 'Al Ghurair Iron &amp; Steel',  'Completed'),
    (7,  'ICAD-1',             'Mussafah, Abu Dhabi','MBS — Meemar Building System', 'Al Ghurair Iron &amp; Steel',  'Completed'),
    (8,  'Kizad',              'Abu Dhabi',          'Capital Engineering Consultant','Cloid Steel Co.',         'Completed'),
    (9,  'ICAD-1',             'Mussafah, Abu Dhabi','MBS — Meemar Building System', 'Al Ghurair Iron &amp; Steel',  'Completed'),
    (10, 'ICAD-1',             'Mussafah, Abu Dhabi','MBS — Meemar Building System', '—',                        'Not yet started'),
]

CLIENTS = ['MBS — Meemar Building System', 'SEWA', 'Al Ghurair Iron &amp; Steel', 'Lamprel',
           'Al Aamedah Al Maseyah', 'Six Sigma', 'Capital Engineering Consultant',
           'Al Aswar Contracting', 'Cloid Steel Co.']

INDUSTRIES = [
    ('Oil, Gas &amp; Petrochemical', 'Pipe spools, tanks, pipe racks and access steel inside live process plant.', 'plant-steel-structure'),
    ('Power &amp; Utilities',        'Substation chequer plate, support steel and enclosures — including work for SEWA.', 'silo-platform-access'),
    ('Ports &amp; Logistics',        'Warehousing, canopies and heavy support steel, including Khalid Port, Sharjah.', 'completed-warehouse'),
    ('Industrial Manufacturing', 'Workshop frames, mezzanines, crane gantries and equipment installation.', 'workshop-interior-crane'),
    ('Cement, Steel &amp; Heavy Materials', 'Silo platforms, conveyor supports and plant structures, including CMW Abu Dhabi.', 'tank-installation-plant'),
    ('Commercial &amp; Infrastructure', 'Car parking shades, handrails, louvers and building maintenance packages.', 'car-parking-shade-row'),
]

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
    ('Nine disciplines, one contract',
     'Steel, piping, tanks, equipment, metalwork, fasteners, supply, manpower and maintenance under a single point of contact.'),
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


def nav(base='', active=None):
    links = ''.join(
        f'<a class="nav__a" href="{base if base and h.startswith("#") else ""}{"index.html" + h if base and h.startswith("#") else h}" data-nav-link>{n}</a>'
        for n, h in NAV)
    mlinks = ''.join(
        f'<a href="{base}index.html{h}" data-nav-link><span class="mono">{i+1:02d}</span>{n}</a>' if base
        else f'<a href="{h}" data-nav-link><span class="mono">{i+1:02d}</span>{n}</a>'
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
  <div class="cta__bg" aria-hidden="true">
    <img src="{base}assets/img/{img}-1400.jpg" alt="" width="1400" height="1400" loading="lazy" decoding="async" data-parallax="-8">
  </div>
  <div class="wrap cta__in">
    <div>
      <p class="eyebrow eyebrow--i" data-reveal>{eyebrow}</p>
      <h2 class="h2 cta__h" style="margin-top:1rem" data-split>{h}</h2>
      <p class="lead lead--i" style="margin-top:1.1rem;max-width:52ch" data-reveal data-delay=".1">{p}</p>
    </div>
    <div style="display:flex;flex-wrap:wrap;gap:.75rem" data-reveal data-delay=".18">
      <a class="btn btn--pri" href="{base}index.html#contact" data-magnet="0.22"><span class="btn__t">Request a quotation</span>{ICON['arrow']}</a>
      <a class="btn btn--ghost-i" href="tel:{PHONE_H}" data-magnet="0.18"><span class="btn__t">{PHONE}</span></a>
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
        <p>Structural steel fabrication, erection, piping, tanks and industrial metalwork — self-performed across the UAE from Dubai and Sharjah.</p>
        <p class="live" style="margin-top:1.1rem;color:var(--t2i)">Dubai licence {LIC_DXB} active</p>
      </div>
      <div class="ft__col">
        <h3>Capability</h3>
        <ul>{svc}<li><a href="{base}index.html#capability">All nine disciplines</a></li></ul>
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
        <li><a href="{base}index.html#contact">Contact</a></li>
      </ul>
    </div>
  </div>
</footer>

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
                "description": "Structural steel fabrication and installation, equipment installation, pipe fabrication, tank installation, miscellaneous metal works, manpower supply, anchor bolt supply, pre-fabricated building supply and building maintenance across the UAE.",
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

    ind = ''.join(f'''
      <div class="ind__row">
        <div class="ind__bg" aria-hidden="true"><img src="assets/img/{im}-800.jpg" alt="" width="800" height="800" loading="lazy" decoding="async"></div>
        <span class="ind__n">{i+1:02d}</span>
        <h3 class="ind__t">{t}</h3>
        <p class="ind__meta">{d}</p>
      </div>''' for i, (t, d, im) in enumerate(INDUSTRIES))

    proc = ''.join(f'''
      <div class="proc__s">
        <span class="proc__bar" aria-hidden="true"></span>
        <p class="proc__n">Step {i+1:02d}</p>
        <h3>{t}</h3>
        <p>{d}</p>
      </div>''' for i, (t, d) in enumerate(PROCESS))

    rows = ''.join(f'''
        <tr>
          <td class="tbl__n">{n:02d}</td>
          <td><span class="tbl__p">{p}</span><span class="tbl__loc">{loc}</span></td>
          <td class="tbl__c">{mc}</td>
          <td class="tbl__c">{cl}</td>
          <td><span class="tbl__st tbl__st--{'done' if st=='Completed' else 'soon'}">{st}</span></td>
        </tr>''' for n, p, loc, mc, cl, st in PROJECTS)

    GAL = ['warehouse-exterior', 'portal-frame-erection', 'fabricated-beams', 'car-parking-shade-row',
           'workshop-interior-crane', 'louver-screen-corner', 'tank-installation-plant', 'curved-roof-erection',
           'completed-warehouse', 'silo-platform-access', 'cladding-blue-facade', 'frame-erection-crane']
    GAL_ALT = ['Completed steel-framed warehouse with cladding and canopy',
               'Portal frame under erection with rafters and purlins in place',
               'Fabricated steel beams and columns marked and stacked for delivery',
               'Row of steel-framed car parking shades with tensioned membrane covering',
               'Workshop interior with overhead crane and steel roof structure',
               'Louvered screen enclosure in coated aluminium',
               'Tank installation with process platform steel and access',
               'Curved roof structure being erected with mobile cranes',
               'Completed clad industrial building with roller shutter opening',
               'Silo platform access steel with cage ladder and handrails',
               'Insulated panel cladding to an industrial facade',
               'Portal frame lifted into position by mobile crane']
    gal = ''.join(f'''
      <figure class="gal__i{' gal__i--w' if i in (0,7) else ''}" data-full="assets/img/{g}-1400.jpg">
        <img src="assets/img/{g}-800.jpg" alt="{a}" width="800" height="800" loading="lazy" decoding="async">
      </figure>''' for i, (g, a) in enumerate(zip(GAL, GAL_ALT)))

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
    desc = ('Structural steel fabrication and erection, equipment and tank installation, pipe fabrication, '
            'metalwork, manpower and building maintenance. Self-performed across Dubai, Sharjah and Abu Dhabi '
            'since 2022.')

    return head(title, desc, SITE + '/', '', jsonld=ld, extra='''
  <link rel="preload" as="image" href="assets/img/og-cover.jpg" fetchpriority="high">
  <script type="importmap">{"imports":{"three":"https://cdn.jsdelivr.net/npm/three@0.160.1/build/three.module.js"}}</script>
  <script type="module" src="assets/js/hero-frame.js"></script>''') + shell_open() + nav() + f'''
<main id="main">

  <!-- ============================================================ HERO -->
  <section class="hero" id="hero">
    <canvas class="hero__canvas" id="hero-canvas" aria-hidden="true"></canvas>
    <div class="hero__glow hero__glow--a" aria-hidden="true"></div>
    <div class="hero__glow hero__glow--b" aria-hidden="true"></div>
    <div class="hero__grad" aria-hidden="true"></div>

    <div class="wrap hero__in">
      <div class="hero__top">
        <div>
          <p class="eyebrow eyebrow--i" data-hero-eye>Dubai · Sharjah · Abu Dhabi — licensed since 2022</p>
          <h1 class="h1 hero__h1" style="margin-top:1.4rem" data-hero-h>Structural steel, fabricated and erected to the grid line.</h1>
        </div>
        <div>
          <p class="lead lead--i hero__sub" data-hero-sub>{CO} fabricates, installs and maintains structural steel, process piping, tanks and industrial metalwork — self-performed by our own workshop and site crews.</p>
          <div class="hero__acts" data-hero-act>
            <a class="btn btn--pri" href="#contact" data-magnet="0.22"><span class="btn__t">Request a quotation</span>{ICON['arrow']}</a>
            <a class="btn btn--ghost-i" href="#capability" data-magnet="0.18"><span class="btn__t">See our capability</span></a>
          </div>
        </div>
      </div>

      <div class="hero__specs" data-hero-spec>
        <div><p class="spec__k">Established</p><p class="spec__v"><span data-count="2022" data-dec="0">2022</span><small>Group workshop licensed in Sharjah</small></p></div>
        <div><p class="spec__k">Disciplines</p><p class="spec__v"><span data-count="9">9</span><small>Steel, piping, tanks, metalwork, more</small></p></div>
        <div><p class="spec__k">Reference projects</p><p class="spec__v"><span data-count="10">10</span><small>Free zones, ports and industrial areas</small></p></div>
        <div><p class="spec__k">Licence status</p><p class="spec__v" style="font-size:clamp(1.1rem,1.7vw,1.4rem)"><span class="live">Active</span><small>Dubai DED {LIC_DXB}</small></p></div>
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
          <p class="lead" data-reveal>Extensive experience in the industry has been fundamental in securing work from corporate companies. We have segmented our main objects into the categories on this page — and we carry them out with our own people.</p>
        </div>
      </div>

      <div class="about__grid">
        <div class="about__body">
          <p data-reveal>{CO} works from two bases: a Sharjah workshop that has held an industrial licence since 2022, and a Dubai contracting licence issued by the Department of Economy and Tourism. Between them they cover fabrication, erection, mechanical installation and maintenance across the Emirates.</p>
          <p data-reveal data-delay=".06">Most of our work reaches site through main contractors and steel suppliers — MBS Meemar Building System, Al Aamedah Al Maseyah, Al Aswar Contracting and Capital Engineering Consultant among them — for end clients including SEWA, Lamprel, Six Sigma and Al Ghurair Iron &amp; Steel. Projects have been delivered in Hamriyah Free Zone, Khalid Port, ICAD-1 Mussafah and Kizad.</p>
          <p data-reveal data-delay=".12">The structure is deliberately simple: our own team carries out the work, without outsourcing or subcontracting. It is the same commitment the company makes on building maintenance, and it applies to every discipline we take on.</p>

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
          <h2 class="h2 shead__title" data-split>Nine disciplines under one contract.</h2>
          <p class="lead" data-reveal>The company profile groups our main objects into six core categories, with supply and maintenance alongside them. Open any discipline for scope, features and the way we price it.</p>
        </div>
      </div>
      <div class="srv">{srv}</div>
      <div class="dim" style="margin-top:2rem">
        <span class="dim__txt">01</span><span class="dim__line"></span>
        <span class="dim__txt">Nine disciplines</span><span class="dim__line"></span><span class="dim__txt">09</span>
      </div>
    </div>
  </section>

  <!-- ======================================================== PRODUCTS -->
  <section class="sec sec--white" id="products">
    <div class="wrap">
      <div class="shead">
        <div class="shead__top"><span class="shead__idx">04</span><p class="eyebrow">Products</p></div>
        <div class="shead__grid">
          <h2 class="h2 shead__title" data-split>Things we make, ready to specify.</h2>
          <p class="lead" data-reveal>Six product families drawn from the metalwork we fabricate most often. Each one is supplied and fixed by the same crews, or supply-only if you have your own installers.</p>
        </div>
      </div>
      <div class="prod" data-stagger>{prod}</div>
    </div>
  </section>

  <!-- ====================================================== INDUSTRIES -->
  <section class="sec sec--ink" id="industries">
    <div class="wrap">
      <div class="shead">
        <div class="shead__top"><span class="shead__idx">05</span><p class="eyebrow eyebrow--i">Industries</p></div>
        <div class="shead__grid">
          <h2 class="h2 shead__title" data-split>Where the steel ends up.</h2>
          <p class="lead lead--i" data-reveal>Six sectors, taken from the projects in our reference list rather than from a brochure.</p>
        </div>
      </div>
      <div class="ind">{ind}</div>
    </div>
  </section>

  <!-- ========================================================= PROCESS -->
  <section class="sec sec--white" id="process">
    <div class="wrap">
      <div class="shead">
        <div class="shead__top"><span class="shead__idx">06</span><p class="eyebrow">Process</p></div>
        <div class="shead__grid">
          <h2 class="h2 shead__title" data-split>Enquiry to handover, in five steps.</h2>
          <p class="lead" data-reveal>The sequence is genuinely sequential — nothing gets cut before drawings are approved, and nothing leaves the workshop out of erection order.</p>
        </div>
      </div>
    </div>
    <div class="wrap"><div class="proc">{proc}</div></div>
  </section>

  <!-- ======================================================== PROJECTS -->
  <section class="sec sec--paper" id="projects">
    <div class="wrap">
      <div class="shead">
        <div class="shead__top"><span class="shead__idx">07</span><p class="eyebrow">Reference projects</p></div>
        <div class="shead__grid">
          <h2 class="h2 shead__title" data-split>Ten projects, named.</h2>
          <p class="lead" data-reveal>Taken directly from our company profile. Contractor and client names are listed as recorded — references available on request.</p>
        </div>
      </div>

      <div class="tbl-wrap" data-rows>
        <table class="tbl">
          <caption class="sr">Reference projects with location, main contractor and client</caption>
          <thead>
            <tr><th scope="col">No.</th><th scope="col">Project / location</th><th scope="col">Main contractor</th><th scope="col">Client</th><th scope="col">Status</th></tr>
          </thead>
          <tbody>{rows}</tbody>
        </table>
      </div>

      <div class="dim" style="margin:clamp(2.5rem,5vw,4rem) 0 1.6rem">
        <span class="dim__txt">Project gallery</span><span class="dim__line"></span><span class="dim__txt">12 frames</span>
      </div>
      <div class="gal" data-stagger>{gal}</div>
      <p class="cap" style="margin-top:1.2rem"><b>Note</b> All photography above is from the ADSD company profile — own fabrication and site work.</p>
    </div>
  </section>

  <!-- ==================================================== TESTIMONIALS -->
  <section class="sec sec--white" id="testimonials">
    <div class="wrap">
      <div class="shead">
        <div class="shead__top"><span class="shead__idx">08</span><p class="eyebrow">In their words</p></div>
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
        <div class="shead__top"><span class="shead__idx">09</span><p class="eyebrow">Questions</p></div>
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
        <div class="shead__top"><span class="shead__idx">10</span><p class="eyebrow eyebrow--i">Contact</p></div>
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
          <div class="cred"><p class="cred__k">Dubai licence — Department of Economy &amp; Tourism</p><p class="cred__v">No. {LIC_DXB} · Technical Services Works · issued 31 March 2022 · <span class="live" style="color:var(--lime)">Active</span></p></div>
          <div class="cred"><p class="cred__k">Group workshop — Sharjah Economic Development Department</p><p class="cred__v">Industrial licence No. {LIC_SHJ} · issued 2022</p></div>
          <div class="cred"><p class="cred__k">Tax registration number</p><p class="cred__v">{TRN}</p></div>
        </div>
      </div>
    </div>
  </section>

</main>
{cta()}
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
        <a class="btn btn--pri" href="#enquire" data-magnet="0.22"><span class="btn__t">Request a quotation</span>{ICON['arrow']}</a>
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
        <a class="tlink" href="#enquire">Enquire about this scope{ICON['arr_sm']}</a>
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
        <a class="tlink" href="{base}index.html#capability">All nine disciplines{ICON['arr_sm']}</a>
      </div>
    </div>
  </section>

  <div id="enquire"></div>
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
        <a class="btn btn--pri" href="#enquire" data-magnet="0.22"><span class="btn__t">Request a quotation</span>{ICON['arrow']}</a>
        <a class="btn btn--ghost-i" href="mailto:{EMAIL}" data-magnet="0.18"><span class="btn__t">{EMAIL}</span></a>
      </div>
    </div>
  </section>

  <section class="sec sec--paper">
    <div class="wrap two">
      <div class="rich">
        <p class="eyebrow" data-reveal>Product overview</p>
        {over}
      </div>
      <aside class="aside" data-reveal>
        <h2 class="h4">Specifications</h2>
        <dl class="specs-tbl">{specs}</dl>
        <p style="font-size:.82rem;color:var(--t3)">Sizes, grades and finishes are confirmed against your drawings or a site survey before quotation.</p>
        <a class="tlink" href="#enquire">Request a quotation{ICON['arr_sm']}</a>
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

  <div id="enquire"></div>
</main>
{cta(base, p['gallery'][1] if len(p['gallery']) > 1 else p['hero'],
     'Enquire', 'Tell us the sizes. We will price the ' + plain.lower() + '.',
     'Send drawings or an opening schedule, or ask us to survey the site. Quotations are free.')}
{footer(base)}'''


# ============================================================== WRITE =====
def write(path, txt):
    with open(os.path.join(OUT, path), 'w', encoding='utf-8') as f:
        f.write(txt)

write('index.html', build_index())
for i, s in enumerate(SERVICES):
    write(f'services/{s["slug"]}.html', build_service(s, i))
for i, p in enumerate(PRODUCTS):
    write(f'products/{p["slug"]}.html', build_product(p, i))

# sitemap + robots
urls = [(SITE + '/', '1.0')]
urls += [(f'{SITE}/services/{s["slug"]}.html', '0.8') for s in SERVICES]
urls += [(f'{SITE}/products/{p["slug"]}.html', '0.8') for p in PRODUCTS]
write('sitemap.xml', '<?xml version="1.0" encoding="UTF-8"?>\n'
      '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
      + ''.join(f'  <url><loc>{u}</loc><priority>{p}</priority></url>\n' for u, p in urls)
      + '</urlset>\n')
write('robots.txt', f'User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n')

print(f'built 1 + {len(SERVICES)} + {len(PRODUCTS)} = {1+len(SERVICES)+len(PRODUCTS)} pages')
