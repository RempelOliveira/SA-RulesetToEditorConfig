from xml.etree import ElementTree

xmlParser = ElementTree.XMLParser(target=ElementTree.TreeBuilder(insert_comments=True))

xmlTree = ElementTree.parse("StyleCopAnalizers.ruleset", parser=xmlParser)
xmlRoot = xmlTree.getroot()

print("")

for xmlRootChild in xmlRoot:
    print("# " + xmlRootChild.attrib["RuleNamespace"])
    print("")

    comments = []
    rulesCodes = []
    rulesValues = []

    for xmlRootChildren in xmlRootChild:
        if xmlRootChildren.text:
            comments.append(xmlRootChildren.text)

        if xmlRootChildren.attrib.get("Id"):
            rulesCodes .append("dotnet_diagnostic." + xmlRootChildren.attrib.get("Id") + ".severity")
            rulesValues.append(xmlRootChildren.attrib.get("Action").lower())

    for i, comment in enumerate(comments):
        print("%-32s %-12s %s" % (rulesCodes[i], "= " + rulesValues[i], "# " + comment))

    print("")
