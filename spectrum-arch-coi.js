const {
  Document, Packer, Paragraph, TextRun, AlignmentType,
  BorderStyle, HeadingLevel, UnderlineType
} = require('docx');
const fs = require('fs');

const BOLD = (text, size) => new TextRun({ text, bold: true, size: size || 24, font: "Times New Roman" });
const NORMAL = (text, size) => new TextRun({ text, size: size || 24, font: "Times New Roman" });
const UNDERLINE = (text) => new TextRun({ text, underline: { type: UnderlineType.SINGLE }, size: 24, font: "Times New Roman" });

const p = (children, opts) => new Paragraph({ children: Array.isArray(children) ? children : [NORMAL(children)], ...opts });
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

      // TITLE
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { after: 0 },
        children: [BOLD("STATE OF NEW YORK", 28)]
      }),
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { after: 0 },
        children: [BOLD("DEPARTMENT OF STATE", 28)]
      }),
      blank(),
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { after: 0 },
        children: [BOLD("CERTIFICATE OF INCORPORATION", 32)]
      }),
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { after: 0 },
        children: [BOLD("OF", 28)]
      }),
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { after: 240 },
        children: [BOLD("SPECTRUM ARCH, INC.", 32)]
      }),
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { after: 480 },
        children: [NORMAL("Under Section 402 of the Not-for-Profit Corporation Law", 24)]
      }),

      // DIVIDER
      new Paragraph({
        border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: "000000", space: 1 } },
        children: [new TextRun("")]
      }),
      blank(),

      // ARTICLE I
      p([BOLD("FIRST: "), NORMAL("The name of the corporation is:")]),
      blank(),
      new Paragraph({
        alignment: AlignmentType.CENTER,
        children: [BOLD("SPECTRUM ARCH, INC.", 28)]
      }),
      blank(),

      // ARTICLE II
      p([BOLD("SECOND: "), NORMAL("This corporation is a Type B not-for-profit corporation as defined in Section 201(b) of the Not-for-Profit Corporation Law.")]),
      blank(),

      // ARTICLE III - PURPOSE
      p([BOLD("THIRD: "), NORMAL("The purposes for which this corporation is formed are exclusively charitable, educational, and scientific within the meaning of Section 501(c)(3) of the Internal Revenue Code of 1986, as amended (the “Code”), including but not limited to the following:")]),
      blank(),
      new Paragraph({
        indent: { left: 720 },
        children: [NORMAL("(a) To develop, operate, manage, and support safe, inclusive, and dignified residential living facilities and community-based programs for adults with autism spectrum disorder (ASD) and other developmental disabilities in New York State;")]
      }),
      blank(),
      new Paragraph({
        indent: { left: 720 },
        children: [NORMAL("(b) To promote the independence, well-being, quality of life, and community integration of adults with autism spectrum disorder and other developmental disabilities through residential services, supported living programs, habilitation services, and related community supports;")]
      }),
      blank(),
      new Paragraph({
        indent: { left: 720 },
        children: [NORMAL("(c) To provide or facilitate the provision of individualized residential alternatives (IRAs), integrated supportive housing, day habilitation, community habilitation, and other services certified or approved by the New York State Office for People With Developmental Disabilities (OPWDD) or its successor agency;")]
      }),
      blank(),
      new Paragraph({
        indent: { left: 720 },
        children: [NORMAL("(d) To raise funds through grants, donations, government contracts, Medicaid reimbursements, and other lawful means to support the corporation’s charitable purposes;")]
      }),
      blank(),
      new Paragraph({
        indent: { left: 720 },
        children: [NORMAL("(e) To educate the public, families, caregivers, and policymakers about the needs and rights of adults with autism spectrum disorder and other developmental disabilities;")]
      }),
      blank(),
      new Paragraph({
        indent: { left: 720 },
        children: [NORMAL("(f) To engage in any and all lawful activities incidental to or in support of the foregoing purposes, provided that such activities are consistent with Section 501(c)(3) of the Code and do not include carrying on propaganda or otherwise attempting to influence legislation (except as permitted under Section 501(h) of the Code), participating in or intervening in any political campaign on behalf of or in opposition to any candidate for public office, or engaging in any other activities not permitted to be carried on by an organization exempt from federal income tax under Section 501(c)(3) of the Code.")]
      }),
      blank(),

      // ARTICLE IV - COUNTY
      p([BOLD("FOURTH: "), NORMAL("The county within the State of New York in which the principal office of the corporation is to be located is "), BOLD("Saratoga County"), NORMAL(".")]),
      blank(),

      // ARTICLE V - SECRETARY OF STATE
      p([BOLD("FIFTH: "), NORMAL("The Secretary of State of the State of New York is hereby designated as the agent of the corporation upon whom process in any action or proceeding against it may be served. The post office address to which the Secretary of State shall mail a copy of any process served upon him or her is:")]),
      blank(),
      new Paragraph({
        indent: { left: 720 },
        children: [NORMAL("Spectrum Arch, Inc.")]
      }),
      new Paragraph({
        indent: { left: 720 },
        children: [NORMAL("29 Westbury Court")]
      }),
      new Paragraph({
        indent: { left: 720 },
        children: [NORMAL("Clifton Park, New York 12065")]
      }),
      blank(),

      // ARTICLE VI - DIRECTORS
      p([BOLD("SIXTH: "), NORMAL("The names and addresses of the persons who are to be the initial directors of the corporation until the first annual meeting of members, or until their successors are elected and qualified, are as follows:")]),
      blank(),
      new Paragraph({
        indent: { left: 720 },
        children: [BOLD("Director 1:")]
      }),
      new Paragraph({ indent: { left: 1080 }, children: [NORMAL("Name: Asad M. Butt")] }),
      new Paragraph({ indent: { left: 1080 }, children: [NORMAL("Address: 29 Westbury Court, Clifton Park, New York 12065")] }),
      blank(),
      new Paragraph({
        indent: { left: 720 },
        children: [BOLD("Director 2:")]
      }),
      new Paragraph({ indent: { left: 1080 }, children: [NORMAL("Name: Tyrone Crooks")] }),
      new Paragraph({ indent: { left: 1080 }, children: [NORMAL("Address: 40 Woodlake Road, Apt. 1, Albany, New York 12203")] }),
      blank(),
      new Paragraph({
        indent: { left: 720 },
        children: [BOLD("Director 3:")]
      }),
      new Paragraph({ indent: { left: 1080 }, children: [NORMAL("Name: Khalid Rehman")] }),
      new Paragraph({ indent: { left: 1080 }, children: [NORMAL("Address: Bergenia House, Feltham, London TW 4GE, United Kingdom")] }),
      blank(),

      // ARTICLE VII - NO PRIVATE INUREMENT
      p([BOLD("SEVENTH: "), NORMAL("No part of the net earnings of the corporation shall inure to the benefit of, or be distributable to, its members, directors, officers, or other private persons, except that the corporation shall be authorized and empowered to pay reasonable compensation for services rendered and to make payments and distributions in furtherance of the purposes set forth in Article THIRD hereof.")]),
      blank(),

      // ARTICLE VIII - DISSOLUTION
      p([BOLD("EIGHTH: "), NORMAL("Upon the dissolution of the corporation, after paying or making provision for the payment of all of the liabilities of the corporation, all of the assets of the corporation shall be distributed exclusively to one or more organizations which are then qualified as exempt organizations under Section 501(c)(3) of the Internal Revenue Code (or the corresponding provision of any future United States Internal Revenue law), as the Board of Directors shall determine. Any such assets not so disposed of shall be disposed of by the Supreme Court of the State of New York in the county in which the principal office of the corporation is then located, exclusively for such purposes or to such organization or organizations, as said Court shall determine, which are organized and operated exclusively for such purposes.")]),
      blank(),

      // ARTICLE IX - LEGISLATIVE ACTIVITY
      p([BOLD("NINTH: "), NORMAL("The corporation shall not carry on any activities not permitted to be carried on by a corporation exempt from federal income tax under Section 501(c)(3) of the Internal Revenue Code, or by a corporation contributions to which are deductible under Section 170(c)(2) of the Internal Revenue Code.")]),
      blank(),

      // ARTICLE X - INCORPORATOR
      p([BOLD("TENTH: "), NORMAL("The name and address of the incorporator is:")]),
      blank(),
      new Paragraph({ indent: { left: 720 }, children: [NORMAL("Name: Asad Munir Butt")] }),
      new Paragraph({ indent: { left: 720 }, children: [NORMAL("Address: 29 Westbury Court, Clifton Park, New York 12065")] }),
      blank(),
      blank(),

      // CERTIFICATION
      new Paragraph({
        border: { top: { style: BorderStyle.SINGLE, size: 6, color: "000000", space: 1 } },
        children: [new TextRun("")]
      }),
      blank(),
      p([NORMAL("IN WITNESS WHEREOF, the undersigned incorporator has executed this Certificate of Incorporation this _____ day of _________________, 2026.")]),
      blank(),
      blank(),
      blank(),
      new Paragraph({
        children: [NORMAL("_________________________________")]
      }),
      new Paragraph({
        children: [BOLD("Asad Munir Butt, Incorporator")]
      }),
      new Paragraph({
        children: [NORMAL("29 Westbury Court")]
      }),
      new Paragraph({
        children: [NORMAL("Clifton Park, New York 12065")]
      }),
      blank(),
      blank(),

      // FILING INSTRUCTIONS
      new Paragraph({
        border: { top: { style: BorderStyle.SINGLE, size: 6, color: "000000", space: 1 } },
        spacing: { before: 240 },
        alignment: AlignmentType.CENTER,
        children: [BOLD("FILING INSTRUCTIONS", 20)]
      }),
      blank(),
      new Paragraph({
        children: [BOLD("Mail to: ", 20), NORMAL("NYS Department of State, Division of Corporations, One Commerce Plaza, 99 Washington Ave, Albany, NY 12231", 20)]
      }),
      new Paragraph({
        children: [BOLD("Filing Fee: ", 20), NORMAL("$75.00 (check or money order payable to “Department of State”)", 20)]
      }),
      new Paragraph({
        children: [BOLD("Online: ", 20), NORMAL("dos.ny.gov (online filing also available)", 20)]
      }),
      new Paragraph({
        children: [BOLD("Note: ", 20), NORMAL("Before filing, complete the addresses for Directors 2 and 3 above. This document must be signed in blue or black ink.", 20)]
      }),
    ]
  }]
});

Packer.toBuffer(doc).then(buffer => {
  fs.writeFileSync("C:\\Users\\Asadm\\Documents\\GSCorp\\SpectrumArch_Certificate_of_Incorporation.docx", buffer);
  console.log("SUCCESS: Document created.");
});
