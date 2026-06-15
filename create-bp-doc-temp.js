const { Document, Packer, Paragraph, TextRun, AlignmentType, HeadingLevel, LevelFormat } = require('docx');
const fs = require('fs');

const BOLD = (text, size) => new TextRun({ text, bold: true, size: size || 24, font: "Calibri" });
const NORMAL = (text, size) => new TextRun({ text, size: size || 24, font: "Calibri" });
const p = (children, opts) => new Paragraph({ children: Array.isArray(children) ? children : [NORMAL(children)], font: "Calibri", ...opts });
const blank = () => new Paragraph({ children: [new TextRun("")] });

const doc = new Document({
  sections: [{
    properties: {
      page: {
        size: { width: 12240, height: 15840 },
        margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 }
      }
    },
    children: [
      // COVER PAGE
      blank(), blank(), blank(),
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { after: 240 },
        children: [new TextRun({ text: "SPECTRUM ARCH, INC.", size: 48, bold: true, font: "Calibri" })]
      }),
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { after: 120 },
        children: [new TextRun({ text: "Business Plan", size: 32, bold: true, font: "Calibri" })]
      }),
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { after: 360 },
        children: [new TextRun({ text: "Residential Services for Adults with Autism", size: 28, font: "Calibri" })]
      }),
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { after: 480 },
        children: [new TextRun({ text: "Capital Region, New York", size: 24, italic: true, font: "Calibri" })]
      }),

      blank(), blank(), blank(),

      p([BOLD("Organization: "), NORMAL("Spectrum Arch, Inc.")]),
      p([BOLD("Address: "), NORMAL("29 Westbury Court, Clifton Park, NY 12065")]),
      p([BOLD("Email: "), NORMAL("info@spectrumarch.org")]),
      p([BOLD("Document Date: "), NORMAL("June 14, 2026")]),

      blank(), blank(), blank(), blank(), blank(),

      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { before: 240 },
        children: [new TextRun({ text: "\"Building the Arch to Independence\"", size: 24, italic: true, bold: true, font: "Calibri" })]
      }),

      new Paragraph({ pageBreakBefore: true, children: [new TextRun("")] }),

      // EXECUTIVE SUMMARY
      new Paragraph({
        heading: HeadingLevel.HEADING_1,
        spacing: { before: 0, after: 240 },
        children: [BOLD("EXECUTIVE SUMMARY", 32)]
      }),

      p("Spectrum Arch, Inc. is a newly incorporated nonprofit organization dedicated to developing and operating residential living facilities and support services for adults with autism spectrum disorder in the Capital Region of New York State."),
      blank(),

      p([BOLD("Mission: "), NORMAL("To promote the independence, dignity, well-being, and community integration of adults with autism spectrum disorder through safe, affirming residential housing and comprehensive support services.")]),
      blank(),

      p([BOLD("Model: "), NORMAL("Individual Residential Alternative (IRA) — state-certified, Medicaid-funded, serving 5–8 residents per home with 24-hour supportive oversight.")]),
      blank(),

      p([BOLD("Target Population: "), NORMAL("Young adults aged 21–30 with autism spectrum disorder and medium-to-high support needs in Saratoga, Albany, and Rensselaer Counties.")]),
      blank(),

      p([BOLD("Revenue Model: "), NORMAL("100% government-funded through Medicaid and OPWDD reimbursement. Expected: $180,000–$220,000 per resident annually.")]),
      blank(),

      new Paragraph({
        heading: HeadingLevel.HEADING_2,
        spacing: { before: 240, after: 120 },
        children: [BOLD("Year 1 Goals (2026)", 26)]
      }),

      new Paragraph({
        numbering: { reference: "bullets", level: 0 },
        children: [NORMAL("Secure 501(c)(3) tax-exempt status from IRS")]
      }),
      new Paragraph({
        numbering: { reference: "bullets", level: 0 },
        children: [NORMAL("Complete OPWDD orientation and begin CRO certification")]
      }),
      new Paragraph({
        numbering: { reference: "bullets", level: 0 },
        children: [NORMAL("Establish board governance and operational policies")]
      }),
      new Paragraph({
        numbering: { reference: "bullets", level: 0 },
        children: [NORMAL("Secure initial grants ($45,000–$50,000)")]
      }),
      new Paragraph({
        numbering: { reference: "bullets", level: 0 },
        children: [NORMAL("Identify and secure property lease")]
      }),
      new Paragraph({
        numbering: { reference: "bullets", level: 0 },
        children: [NORMAL("Build operational foundation for Year 2 launch")]
      }),

      blank(),

      new Paragraph({
        heading: HeadingLevel.HEADING_2,
        spacing: { before: 240, after: 120 },
        children: [BOLD("Year 2 & 3 Goals", 26)]
      }),

      p([BOLD("Year 2: "), NORMAL("Achieve OPWDD certification, hire core staff (6 FTE), admit first 3–4 residents, stabilize operations ($375K revenue).")]),
      p([BOLD("Year 3: "), NORMAL("Scale to full capacity (5–8 residents), demonstrate impact, explore replication ($1.1M revenue, $609K surplus).")]),

      new Paragraph({ pageBreakBefore: true, children: [new TextRun("")] }),

      // SECTION 1
      new Paragraph({
        heading: HeadingLevel.HEADING_1,
        spacing: { before: 0, after: 240 },
        children: [BOLD("SECTION 1: THE IRA MODEL", 32)]
      }),

      new Paragraph({
        heading: HeadingLevel.HEADING_2,
        spacing: { before: 240, after: 120 },
        children: [BOLD("What is an IRA?", 26)]
      }),

      p("An Individual Residential Alternative (IRA) is a state-certified residential service model serving 2–8 residents in a home with 24-hour staff support, Medicaid funding, and OPWDD oversight. Key characteristics:"),
      blank(),

      new Paragraph({
        numbering: { reference: "bullets", level: 0 },
        children: [NORMAL("Small group home (2–8 residents) in community setting")]
      }),
      new Paragraph({
        numbering: { reference: "bullets", level: 0 },
        children: [NORMAL("24-hour staff presence with trained Direct Support Professionals")]
      }),
      new Paragraph({
        numbering: { reference: "bullets", level: 0 },
        children: [NORMAL("100% funded through Medicaid — no private fees")]
      }),
      new Paragraph({
        numbering: { reference: "bullets", level: 0 },
        children: [NORMAL("Requires OPWDD certification and annual inspections")]
      }),
      new Paragraph({
        numbering: { reference: "bullets", level: 0 },
        children: [NORMAL("Services: daily living support, community integration, employment coaching")]
      }),

      blank(),

      new Paragraph({
        heading: HeadingLevel.HEADING_2,
        spacing: { before: 240, after: 120 },
        children: [BOLD("Why Spectrum Arch Chose IRA", 26)]
      }),

      new Paragraph({
        numbering: { reference: "numbers", level: 0 },
        children: [NORMAL("Highest Medicaid reimbursement — $180K–$220K per resident/year")]
      }),
      new Paragraph({
        numbering: { reference: "numbers", level: 0 },
        children: [NORMAL("Clearest regulatory pathway — OPWDD process well-established")]
      }),
      new Paragraph({
        numbering: { reference: "numbers", level: 0 },
        children: [NORMAL("Highly focused market — 200–300 young adults in Capital Region aging out of school")]
      }),
      new Paragraph({
        numbering: { reference: "numbers", level: 0 },
        children: [NORMAL("Best outcomes for medium-high support individuals")]
      }),

      new Paragraph({ pageBreakBefore: true, children: [new TextRun("")] }),

      // SECTION 2
      new Paragraph({
        heading: HeadingLevel.HEADING_1,
        spacing: { before: 0, after: 240 },
        children: [BOLD("SECTION 2: TARGET POPULATION & MARKET", 32)]
      }),

      new Paragraph({
        heading: HeadingLevel.HEADING_2,
        spacing: { before: 240, after: 120 },
        children: [BOLD("Who We Serve", 26)]
      }),

      p([BOLD("Age Range: "), NORMAL("21–30 years old (young adults transitioning from school to community)")]),
      p([BOLD("Diagnosis: "), NORMAL("Autism Spectrum Disorder (confirmed DSM-5)")]),
      p([BOLD("Support Level: "), NORMAL("Medium to high — require daily assistance but not intensive medical care")]),
      p([BOLD("Geography: "), NORMAL("Saratoga, Albany, Rensselaer Counties (Capital Region)")]),

      blank(),

      new Paragraph({
        heading: HeadingLevel.HEADING_2,
        spacing: { before: 240, after: 120 },
        children: [BOLD("Market Demand", 26)]
      }),

      p([BOLD("The Crisis: "), NORMAL("Young adults with autism 'age out' of school at 21 with zero housing or day program options. This 21–30 cohort faces the most acute need: families desperate for solutions, individuals ready for community living, and government highest support availability. After age 30, fewer young people enter the system; ages 21–30 represent the critical window for placement.")]),

      blank(),

      p([BOLD("Capital Region Data:"), NORMAL("")]),
      new Paragraph({
        numbering: { reference: "bullets", level: 0 },
        children: [NORMAL("~2,000+ adults with autism in 3-county region")]
      }),
      new Paragraph({
        numbering: { reference: "bullets", level: 0 },
        children: [NORMAL("~200–300 in critical age range (21–30) — the \"aging out\" cohort")]
      }),
      new Paragraph({
        numbering: { reference: "bullets", level: 0 },
        children: [NORMAL("Fewer than 50 residential slots exist")]
      }),
      new Paragraph({
        numbering: { reference: "bullets", level: 0 },
        children: [NORMAL("Waiting list: 18–36 months for OPWDD services")]
      }),
      new Paragraph({
        numbering: { reference: "bullets", level: 0 },
        children: [NORMAL("Families desperately seeking quality, affordable options")]
      }),

      new Paragraph({ pageBreakBefore: true, children: [new TextRun("")] }),

      // SECTION 3
      new Paragraph({
        heading: HeadingLevel.HEADING_1,
        spacing: { before: 0, after: 240 },
        children: [BOLD("SECTION 3: OPERATIONS & STAFFING", 32)]
      }),

      new Paragraph({
        heading: HeadingLevel.HEADING_2,
        spacing: { before: 240, after: 120 },
        children: [BOLD("A 6-Resident Home", 26)]
      }),

      p([BOLD("Physical: "), NORMAL("Single-family home or duplex with 6 bedrooms, common areas, kitchen, ADA-accessible, located in community.")]),

      p([BOLD("Daily Operations: "), NORMAL("Staff support residents with waking, hygiene, meals, medication, appointments, employment/day programs, community outings, evening activities, overnight supervision.")]),

      blank(),

      new Paragraph({
        heading: HeadingLevel.HEADING_2,
        spacing: { before: 240, after: 120 },
        children: [BOLD("Staffing (6-Resident Home)", 26)]
      }),

      p("All salaries funded from Medicaid reimbursement — zero startup capital required:"),
      blank(),

      new Paragraph({
        numbering: { reference: "bullets", level: 0 },
        children: [NORMAL("Program Director: 1.0 FTE @ $55,000 (oversight, hiring, compliance)")]
      }),
      new Paragraph({
        numbering: { reference: "bullets", level: 0 },
        children: [NORMAL("Lead DSP (Shift Lead): 1.0 FTE @ $42,000 (supervision, training)")]
      }),
      new Paragraph({
        numbering: { reference: "bullets", level: 0 },
        children: [NORMAL("DSP (Evening/Community): 1.5 FTE @ $42,000 (direct care, community)")]
      }),
      new Paragraph({
        numbering: { reference: "bullets", level: 0 },
        children: [NORMAL("DSP (Day Support): 1.5 FTE @ $42,000 (daytime activities, employment)")]
      }),
      new Paragraph({
        numbering: { reference: "bullets", level: 0 },
        children: [NORMAL("Night Staff (Overnight): 0.5 FTE @ $40,000 (overnight supervision)")]
      }),
      new Paragraph({
        numbering: { reference: "bullets", level: 0 },
        children: [NORMAL("Admin/Bookkeeper: 0.5 FTE @ $38,000 (scheduling, billing, records)")]
      }),

      blank(),

      p([BOLD("Total: "), NORMAL("6.0 FTE, ~$259,000/year — fully covered by Medicaid reimbursement")]),

      new Paragraph({ pageBreakBefore: true, children: [new TextRun("")] }),

      // SECTION 4
      new Paragraph({
        heading: HeadingLevel.HEADING_1,
        spacing: { before: 0, after: 240 },
        children: [BOLD("SECTION 4: FINANCIAL PROJECTIONS", 32)]
      }),

      new Paragraph({
        heading: HeadingLevel.HEADING_2,
        spacing: { before: 240, after: 120 },
        children: [BOLD("Medicaid Rates (Capital Region, 2026)", 26)]
      }),

      p([BOLD("Per Resident Per Year: "), NORMAL("$180,000–$220,000 (based on daily rate of $480–$600)")]),
      p([BOLD("Planning Estimate: "), NORMAL("$180,000 per resident per year (conservative)")]),

      blank(),

      new Paragraph({
        heading: HeadingLevel.HEADING_2,
        spacing: { before: 240, after: 120 },
        children: [BOLD("Year 1 (2026): Setup Phase", 26)]
      }),

      p([BOLD("Revenue: "), NORMAL("$45,000–$50,000 (GRSCorp $20K, Google Ads $10K, Microsoft $5K, Foundation grants $10–15K)")]),
      p([BOLD("Expenses: "), NORMAL("~$37,000–$40,000 (Legal, OPWDD, insurance, property search, staff recruitment, marketing, training)")]),
      p([BOLD("Net: "), NORMAL("$5,000–$13,000 surplus for reserves")]),

      blank(),

      new Paragraph({
        heading: HeadingLevel.HEADING_2,
        spacing: { before: 240, after: 120 },
        children: [BOLD("Year 2 (2027): Launch Phase", 26)]
      }),

      p([BOLD("Revenue: "), NORMAL("$375,000 (4 residents × $180K × 0.5 year + grants $15K)")]),
      p([BOLD("Expenses: "), NORMAL("~$220,000 (prorated staffing $130K, lease $36K, utilities $18K, insurance $8K, training $5K, admin $8K, contingency $15K)")]),
      p([BOLD("Net: "), NORMAL("~$155,000 reinvested in operations and reserves")]),

      blank(),

      new Paragraph({
        heading: HeadingLevel.HEADING_2,
        spacing: { before: 240, after: 120 },
        children: [BOLD("Year 3 (2028): Full Operation", 26)]
      }),

      p([BOLD("Revenue: "), NORMAL("~$1,100,000 (6 residents × $180K + grants $20K)")]),
      p([BOLD("Expenses: "), NORMAL("~$491,000 (full staffing $259K, lease $72K, utilities $72K, insurance $18K, legal/training/admin $20K, reserves $50K)")]),
      p([BOLD("Net: "), NORMAL("~$609,000+ available for expansion, second home, or endowment")]),

      blank(),

      p([BOLD("Break-Even: "), NORMAL("3 residents at full Medicaid rate (~$540K/year) covers all operating costs")]),
      p([BOLD("Margin: "), NORMAL("Each resident 4–6 after break-even yields ~$140K–$180K net margin (80% contribution)")]),

      new Paragraph({ pageBreakBefore: true, children: [new TextRun("")] }),

      // SECTION 5
      new Paragraph({
        heading: HeadingLevel.HEADING_1,
        spacing: { before: 0, after: 240 },
        children: [BOLD("SECTION 5: TIMELINE", 32)]
      }),

      p([BOLD("Q2 2026 (NOW): "), NORMAL("Certificate of Incorporation filed ✅. Apply for EIN. Begin 501c3 application. Board meeting.")]),
      blank(),
      p([BOLD("Q3 2026: "), NORMAL("Complete 501c3 status. OPWDD orientation. Begin CRO application. Board committees established.")]),
      blank(),
      p([BOLD("Q4 2026: "), NORMAL("Submit OPWDD CRO application. Property search. Google Ad Grants live. Foundation grants applied.")]),
      blank(),
      p([BOLD("Q1 2027: "), NORMAL("OPWDD pre-certification. Property lease signed. OPWDD certification approved. Program Director hired. Staff recruitment.")]),
      blank(),
      p([BOLD("Q2–Q3 2027: "), NORMAL("Staff training. First 3–4 residents admitted (July/August). Operations launch.")]),
      blank(),
      p([BOLD("Q4 2027: "), NORMAL("Stabilize first cohort. Outcome measurement. Plan for expansion.")]),

      new Paragraph({ pageBreakBefore: true, children: [new TextRun("")] }),

      // SECTION 6
      new Paragraph({
        heading: HeadingLevel.HEADING_1,
        spacing: { before: 0, after: 240 },
        children: [BOLD("SECTION 6: GOVERNANCE", 32)]
      }),

      new Paragraph({
        heading: HeadingLevel.HEADING_2,
        spacing: { before: 240, after: 120 },
        children: [BOLD("Board of Directors", 26)]
      }),

      p([BOLD("Asad M. Butt "), NORMAL("(Founder, President) — 29 Westbury Court, Clifton Park, NY 12065")]),
      p([BOLD("Tyrone Crooks "), NORMAL("(Director, Independent) — 40 Woodlake Road, Apt 1, Albany, NY 12203")]),
      p([BOLD("Khalid Rehman "), NORMAL("(Director, Independent) — Bergenia House, Feltham, London TW13 4GE, UK")]),

      blank(),

      p("Committees: Finance & Audit | Governance & Compliance | Programs & Quality"),

      blank(),

      new Paragraph({
        heading: HeadingLevel.HEADING_2,
        spacing: { before: 240, after: 120 },
        children: [BOLD("GRSCorp's Role", 26)]
      }),

      p("GRSCorp (private foundation) will make qualifying distributions to Spectrum Arch for Year 1 startup: $20,000 for legal setup, OPWDD orientation, property search, staff recruitment, initial marketing. Year 2 forward: Spectrum Arch self-sufficient through Medicaid."),

      new Paragraph({ pageBreakBefore: true, children: [new TextRun("")] }),

      // CONCLUSION
      new Paragraph({
        heading: HeadingLevel.HEADING_1,
        spacing: { before: 0, after: 240 },
        children: [BOLD("CONCLUSION", 32)]
      }),

      p("Spectrum Arch, Inc. addresses a critical unmet need: safe, high-quality residential housing for adults with autism in the Capital Region. The IRA model is proven, well-funded through Medicaid, and aligns with New York State priorities."),

      blank(),

      p("With a strong nonprofit foundation, clear operational plan, and commitment to person-centered care, Spectrum Arch will serve as a model provider for decades."),

      blank(),

      p([BOLD("2031 Vision: "), NORMAL("3–4 homes serving 20+ residents, documented outcomes showing improved independence and community integration. Trusted partner for families and OPWDD.")]),

      blank(), blank(),

      p([BOLD("Next Steps:"), NORMAL("")]),
      new Paragraph({
        numbering: { reference: "numbers", level: 0 },
        children: [NORMAL("Board approval (July 2026)")]
      }),
      new Paragraph({
        numbering: { reference: "numbers", level: 0 },
        children: [NORMAL("Share with OPWDD at orientation (August 2026)")]
      }),
      new Paragraph({
        numbering: { reference: "numbers", level: 0 },
        children: [NORMAL("Use for grant applications (Q3–Q4 2026)")]
      }),
      new Paragraph({
        numbering: { reference: "numbers", level: 0 },
        children: [NORMAL("Reference for staff recruitment (Q1 2027)")]
      }),
      new Paragraph({
        numbering: { reference: "numbers", level: 0 },
        children: [NORMAL("Update annually")]
      }),

      blank(), blank(), blank(),

      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { before: 240, after: 0 },
        children: [new TextRun({ text: "\"Building the Arch to Independence\"", size: 24, italic: true, bold: true, color: "2E75B6" })]
      }),
      new Paragraph({
        alignment: AlignmentType.CENTER,
        children: [new TextRun({ text: "Spectrum Arch, Inc. | info@spectrumarch.org | spectrumarch.org", size: 20, italic: true, color: "666666" })]
      }),
    ]
  }],

  numbering: {
    config: [
      {
        reference: "bullets",
        levels: [{
          level: 0,
          format: LevelFormat.BULLET,
          text: "•",
          alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 720, hanging: 360 } } }
        }]
      },
      {
        reference: "numbers",
        levels: [{
          level: 0,
          format: LevelFormat.DECIMAL,
          text: "%1.",
          alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 720, hanging: 360 } } }
        }]
      },
    ]
  }
});

Packer.toBuffer(doc).then(buffer => {
  fs.writeFileSync("C:\\Users\\Asadm\\Documents\\GSCorp\\Spectrum_Arch_Business_Plan_UPDATED.docx", buffer);
  console.log("✅ Professional Word document created successfully!");
});
