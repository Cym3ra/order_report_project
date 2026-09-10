# Reflektion

**Vilka var de viktigaste problemen i originalkoden?**

De största problemen i originalprogrammet var att all logik låg i en och samma fil, felhanteringen var för bred och rapporteringen innehöll duplicerad kod.

**Vilka förändringar tycker du förbättrade programmet mest?**

Att separera programmets olika ansvar, vilket gör koden lättare att förstå, testa och vidareutveckla. 
Att ersätta print() med logging gör det också möjligt att få tydliga och relevanta varningar om problem uppstår i datan.

**Varför valde du den projektstruktur du använde?**

Jag valde den strukturen jag gjorde då den är tydlig med vilka ansvarsområden varje fil har.

**Var använde du OOP/dataclass och varför passade det där?**

Jag använder ReportConfig som dataclass för att samla programmets konfiguration. Det ger ett tydligt ansvar av programmets input och output utan att skapa en onödigt stor klass.

**Vilka viktiga beteenden skyddar dina automatiska tester, och vilken nytta ger testerna om programmet förändras i framtiden?**

Testerna kontrollerar bland annat beräkningen av ordervärden, hantering av saknade värden, saknade värden, negativa värden.

Testerna innehåller både normala fall och felscenarier. Om programmet förändras i framtiden kan testerna upptäcka om något gått sönder i koden.

**Vad var svårast?**

Att dela upp koden utan att ändra på programmets befintliga beräkningar och resultat. Att varje fil ska ha ett tydligt ansvar -  dock utan att skapa för många små filer. Samt testerna, vad man ska testa och hur de ska skapas.

**Vad hade du velat förbättra ytterligare om du haft mer tid?**

Skapa fler tester, både rimliga och felscenario varianter. Kanske skapat en lite mer avancerad validering. Sen kanske lite mer logging när det gäller ogiltiga värden, som ändras till NaN och liknande för att inte skapa fel i körningen.

