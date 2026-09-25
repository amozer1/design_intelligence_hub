import streamlit as st

def get_metrics(cl32):

    DELIVERABLE_NAMES = [
        "Outfall pipework optioneering",
        "Model Existing Tank",
        "Build Terrain Model",
        "BIM Set Up",
        "Civil Modelling - Tank",
        "Civil Modelling - Other Assets",
        "Mechanical Modelling",
        "Network modelling",
        "BIM Execution Plan",
        "Determine entry/exit levels",
        "Review GI",
        "Estimate conservative thickness",
        "Assessment to determine",
        "Check on shaft sizing",
        "Produce 2D conept drawing",
        "MGE Detailed Pile Design",
        "CAT2 check on MGE pile design",
        "Manhole Schedule",
        "Outline drawing",
        "GA & Long sections",
        "Valve chamber standard detail",
        "Kiosk slab proposal",
        "Shaft penetrations",
        "Line sizing",
        "Mechanical calculations",
        "Pump system curve",
        "Basis of Design",
        "Outline P&IDs",
        "Control Philosophy",
        "Submission of Outline Design Pack",
        "Client Review of Design Pack",
        "Review available GI",
        "GDR",
        "Client Review of GDR",
        "Benching design",
        "Cover slab design",
        "Pipe entry/exit",
        "Pipe exit details",
        "MH01 & MH02 Design",
        "Pipework from MHs to Shaft",
        "Valve Chamber",
        "Flowmeter Chamber",
        "Civils Pipe Design",
        "Tank kiosk enclosure foundation",
        "Assessment of exit details",
        "Routing & Design",
        "HAZOP",
        "DSEAR Assessment",
        "Material Take Off",
        "User Requirement Specification",
        "Load Schedule",
        "Power Supply Assessment",
        "Network Architecture Drawing",
        "Telemetry Schedules",
        "Single Line Diagrams",
        "Block Cable Diagrams",
        "Final Submission",
    ]

    names = (
        cl32["Activity Name"]
        .fillna("")
        .astype(str)
        .str.strip()
    )

    matched = set()

    for name in names:

        for deliverable in DELIVERABLE_NAMES:

            if deliverable.lower() in name.lower():
                matched.add(deliverable)
                break

    return {
        "total_deliverables": len(matched)
    }