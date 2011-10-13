from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext import db
import datetime
import entities
import htmlHelper

class InsertRoot(webapp.RequestHandler):
    def get(self):
        self.response.out.write(htmlHelper.header())
        self.response.out.write(htmlHelper.insertRootLink("Afspraak"))
        self.response.out.write(htmlHelper.insertRootLink("Docent"))
        self.response.out.write(htmlHelper.insertRootLink("Vak"))
        self.response.out.write(htmlHelper.insertRootLink("VakPerKlas"))
        self.response.out.write(htmlHelper.footer())

class InsertAfspraak(webapp.RequestHandler):
    def get(self):
        self.response.out.write(htmlHelper.header())
        afspraken = entities.Afspraak.all()
        if(afspraken.count() == 0):
            afspraak = entities.Afspraak(leerlingID="1234",docentID='BAARR',dag=datetime.date(2011, 10, 11), tijd=-1,tafelnummer=0,beschrijving='test')
            afspraak.put();
            afspraak = entities.Afspraak(leerlingID="1234",docentID='BAARR',dag=datetime.date(2011, 10, 12), tijd=-1,tafelnummer=0,beschrijving='test')
            afspraak.put();
            afspraak = entities.Afspraak(leerlingID="1234",docentID='BAARR',dag=datetime.date(2011, 10, 13), tijd=-1,tafelnummer=0,beschrijving='test')
            afspraak.put();
            afspraak = entities.Afspraak(leerlingID="1234",docentID='BAARR',dag=datetime.date(2011, 10, 14), tijd=-1,tafelnummer=0,beschrijving='test')
            afspraak.put();
            afspraak = entities.Afspraak(leerlingID="1235",docentID='BABER',dag=datetime.date(2011, 10, 11), tijd=-1,tafelnummer=0,beschrijving='test')
            afspraak.put();
            afspraak = entities.Afspraak(leerlingID="1235",docentID='BABER',dag=datetime.date(2011, 10, 12), tijd=-1,tafelnummer=0,beschrijving='test')
            afspraak.put();
            afspraak = entities.Afspraak(leerlingID="1235",docentID='BABER',dag=datetime.date(2011, 10, 13), tijd=-1,tafelnummer=0,beschrijving='test')
            afspraak.put();
            afspraak = entities.Afspraak(leerlingID="1235",docentID='BACUL',dag=datetime.date(2011, 10, 11), tijd=-1,tafelnummer=0,beschrijving='test')
            afspraak.put();
            afspraak = entities.Afspraak(leerlingID="1235",docentID='BACUL',dag=datetime.date(2011, 10, 12), tijd=-1,tafelnummer=0,beschrijving='test')
            afspraak.put();
            afspraak = entities.Afspraak(leerlingID="1235",docentID='BACUL',dag=datetime.date(2011, 10, 13), tijd=-1,tafelnummer=0,beschrijving='test')
            afspraak.put();
            afspraak = entities.Afspraak(leerlingID="1235",docentID='BAKAX',dag=datetime.date(2011, 10, 11), tijd=-1,tafelnummer=0,beschrijving='test')
            afspraak.put();
            afspraak = entities.Afspraak(leerlingID="1235",docentID='BAKAX',dag=datetime.date(2011, 10, 12), tijd=-1,tafelnummer=0,beschrijving='test')
            afspraak.put();
            afspraak = entities.Afspraak(leerlingID="1235",docentID='BAKAX',dag=datetime.date(2011, 10, 13), tijd=-1,tafelnummer=0,beschrijving='test')
            afspraak.put();
            afspraak = entities.Afspraak(leerlingID="1235",docentID='BAKET',dag=datetime.date(2011, 10, 11), tijd=-1,tafelnummer=0,beschrijving='test')
            afspraak.put();
            afspraak = entities.Afspraak(leerlingID="1235",docentID='BAKET',dag=datetime.date(2011, 10, 12), tijd=-1,tafelnummer=0,beschrijving='test')
            afspraak.put();
            afspraak = entities.Afspraak(leerlingID="1235",docentID='BAKET',dag=datetime.date(2011, 10, 13), tijd=-1,tafelnummer=0,beschrijving='test')
            afspraak.put();
            
            self.response.out.write('Afspraken toegevoegd aan de datastore')
        else:
            self.response.out.write(htmlHelper.startTable(header=['leerlingID','DocentID','dag','Tijd','Tafelnummer','beschrijving']))
            for afspraak in afspraken:
                self.response.out.write("<tr>")
                self.response.out.write("<td>"+afspraak.leerlingID+"</td>")
                self.response.out.write("<td>"+afspraak.docentID+"</td>")
                self.response.out.write("<td>"+str(afspraak.dag)+"</td>")
                self.response.out.write("<td>"+str(afspraak.tijd)+"</td>")
                self.response.out.write("<td>"+str(afspraak.tafelnummer)+"</td>")
                self.response.out.write("<td>"+afspraak.beschrijving+"</td>")
                self.response.out.write("</tr>")
            self.response.out.write("</table>")
            self.response.out.write("<form action='/insert/afspraakpost' method='post'><input type='hidden' name='delete' value='delete' /><input type='submit' value='Delete All' /></form")
            self.response.out.write(htmlHelper.footer())

class InsertDocent(webapp.RequestHandler):
    def get(self):
        self.response.out.write(htmlHelper.header())
        docenten = entities.Docent.all()
        if(docenten.count() == 0):
            docent = entities.Docent(docentID='BAARR', aanhef='mw. drs.', naam='R.Baart', postvaknummer=41, email='BAARR@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BABER', aanhef='dhr.', naam='R.Babel', postvaknummer=48, email='BABER@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BACUL', aanhef='dhr.', naam='L.Bacuna', postvaknummer=55, email='BACUL@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BAKAX', aanhef='dhr.', naam='A.Bak', postvaknummer=62, email='BAKAX@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BAKET', aanhef='dhr.', naam='T.Bakens', postvaknummer=69, email='BAKET@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BAKHB', aanhef='mw.', naam='B.B.Bakhuys', postvaknummer=76, email='BAKHB@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BAKKO', aanhef='mw.', naam='O.O.Bakkal', postvaknummer=83, email='BAKKO@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BAKKY', aanhef='dhr. ir.', naam='Y.Bakkati', postvaknummer=90, email='BAKKY@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BAKKB', aanhef='mw. drs.', naam='B.Z.N.Bakker', postvaknummer=97, email='BAKKB@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BAKXI', aanhef='dhr. mr.', naam='I.C.Bakx', postvaknummer=104, email='BAKXI@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BALSG', aanhef='dhr.', naam='G.Bals', postvaknummer=111, email='BALSG@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BARAA', aanhef='mw. drs.', naam='A.Barakat', postvaknummer=118, email='BARAA@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BAREJ', aanhef='dhr. drs.', naam='J. Barendregt', postvaknummer=4, email='BAREJ@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BARTL', aanhef='mw.', naam='L.Barth', postvaknummer=11, email='BARTL@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BARNJ', aanhef='dhr. drs.', naam='J. van Barneveld', postvaknummer=18, email='BARNJ@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BASTM', aanhef='mw.', naam='M. van Basten', postvaknummer=25, email='BASTM@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BEEKC', aanhef='dhr.', naam='C.C.Beekink', postvaknummer=32, email='BEEKC@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BEEND', aanhef='dhr.', naam='D.Been', postvaknummer=39, email='BEEND@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BEENM', aanhef='dhr.', naam='M.Been', postvaknummer=46, email='BEENM@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BEENL', aanhef='dhr. dr. ir.', naam='L.Beenhakker', postvaknummer=53, email='BEENL@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BEERR', aanhef='dhr.', naam='R.Beerens', postvaknummer=60, email='BEERR@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BENOA', aanhef='dhr. ir.', naam='A.Benomar', postvaknummer=67, email='BENOA@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BEELM', aanhef='dhr.', naam='M.M.M.Beelenkamp', postvaknummer=74, email='BEELM@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BERGP', aanhef='mw. drs.', naam='P. van den Berg', postvaknummer=81, email='BERGP@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BERGR', aanhef='mw. drs.', naam='R. van den Berg', postvaknummer=88, email='BERGR@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BERGD', aanhef='dhr.', naam='D. van den Bergh', postvaknummer=95, email='BERGD@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BERGH', aanhef='mw.', naam='R.N.A. van den Bergh', postvaknummer=102, email='BERGH@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BERGG', aanhef='dhr.', naam='G.Bergholtz', postvaknummer=109, email='BERGG@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BERGF', aanhef='dhr.', naam='F.Berghuis', postvaknummer=116, email='BERGF@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BERGX', aanhef='dhr.', naam='X.Bergkamp', postvaknummer=2, email='BERGX@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BERRE', aanhef='mw.', naam='R.E.T.Bergkamp', postvaknummer=9, email='BERRE@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BEUKR', aanhef='dhr. drs.', naam='R.Beukenkamp', postvaknummer=16, email='BEUKR@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BEUKJ', aanhef='dhr. ir.', naam='J. van Beukering', postvaknummer=23, email='BEUKJ@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BEVEJ', aanhef='dhr.', naam='J.H.M. van Beveren', postvaknummer=30, email='BEVEJ@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BEVEW', aanhef='dhr.', naam='W. van Beveren', postvaknummer=37, email='BEVEW@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BIESL', aanhef='mw. drs.', naam='L.Biesbrouck', postvaknummer=44, email='BIESL@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BISCF', aanhef='mw.', naam='F.Bischot', postvaknummer=51, email='BISCF@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BISED', aanhef='mw.', naam='D.Biseswar', postvaknummer=58, email='BISED@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BIYAM', aanhef='dhr.', naam='M.Biyadat', postvaknummer=65, email='BIYAM@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BLANF', aanhef='dhr.', naam='F.Blankemeijer', postvaknummer=72, email='BLANF@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BLEWW', aanhef='mw. drs.', naam='W.W.Bleijenberg', postvaknummer=79, email='BLEWW@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BLEUE', aanhef='dhr.', naam='E.Bleuming', postvaknummer=86, email='BLEUE@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BLIND', aanhef='dhr.', naam='D.Blind', postvaknummer=93, email='BLIND@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BLINR', aanhef='dhr.', naam='R.Blinker', postvaknummer=100, email='BLINR@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BLOEB', aanhef='dhr. drs.', naam='B.B.Bloemendaal', postvaknummer=107, email='BLOEB@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BLUMH', aanhef='dhr.', naam='H.Blume', postvaknummer=114, email='BLUMH@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BOATG', aanhef='mw.', naam='G.Boateng', postvaknummer=0, email='BOATG@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BOBSK', aanhef='mw.', naam='K.Bobson', postvaknummer=7, email='BOBSK@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BODDF', aanhef='mw. drs.', naam='F.Bodde', postvaknummer=14, email='BODDF@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BOEKL', aanhef='dhr.', naam='L. te Boekhorst', postvaknummer=21, email='BOEKL@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BOEKC', aanhef='dhr. ir.', naam='C. Boekweg', postvaknummer=28, email='BOEKC@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BOERD', aanhef='dhr.', naam='D. de Boer', postvaknummer=35, email='BOERD@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BOERY', aanhef='mw.', naam='Y. Boer', postvaknummer=42, email='BOERY@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BOERR', aanhef='dhr.', naam='R. de Boer', postvaknummer=49, email='BOERR@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BOERJ', aanhef='dhr. ir.', naam='J. Boere', postvaknummer=56, email='BOERJ@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BOERM', aanhef='dhr. ir.', naam='M. Boerebach', postvaknummer=63, email='BOERM@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BOERA', aanhef='dhr.', naam='A. Boersma', postvaknummer=70, email='BOERA@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BOEVP', aanhef='dhr.', naam='P. Boeve', postvaknummer=77, email='BOEVP@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BOGAW', aanhef='dhr.', naam='W. Bogarde', postvaknummer=84, email='BOGAW@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BOMMM', aanhef='mw. drs.', naam='M. van Bommel', postvaknummer=91, email='BOMMM@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BONSO', aanhef='dhr. drs.', naam='O. Bonsema', postvaknummer=98, email='BONSO@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BOOGM', aanhef='dhr.', naam='M. van den Boogaart', postvaknummer=105, email='BOOGM@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BOOGE', aanhef='dhr.', naam='M. Boogers', postvaknummer=112, email='BOOGE@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BOOYF', aanhef='dhr. ir.', naam='F. Booy', postvaknummer=119, email='BOOYF@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BOSCS', aanhef='dhr. ir.', naam='S. Boschker', postvaknummer=5, email='BOSCS@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BOSKH', aanhef='dhr.', naam='H. Boskamp', postvaknummer=12, email='BOSKH@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BOSKJ', aanhef='dhr.', naam='J. Boskamp', postvaknummer=19, email='BOSKJ@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BOSMJ', aanhef='mw.', naam='J. Bosman', postvaknummer=26, email='BOSMJ@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BOSSP', aanhef='mw.', naam='P. Bosschaart', postvaknummer=33, email='BOSSP@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BOSVG', aanhef='mw.', naam='G. Bosveld', postvaknummer=40, email='BOSVG@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BOSVH', aanhef='mw.', naam='H. Bosveld', postvaknummer=47, email='BOSVH@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BOSVP', aanhef='dhr. dr.', naam='P. Bosvelt', postvaknummer=54, email='BOSVP@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BOSZP', aanhef='dhr.', naam='P. Bosz', postvaknummer=61, email='BOSZP@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BOTRR', aanhef='dhr. ir.', naam='R. Bot', postvaknummer=68, email='BOTRR@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BOVED', aanhef='mw. drs.', naam='D. Bovenberg', postvaknummer=75, email='BOVED@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BOUCE', aanhef='dhr. drs.', naam='E. Bouchiba', postvaknummer=82, email='BOUCE@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BOULK', aanhef='dhr. ir.', naam='K. Boulahrouz', postvaknummer=89, email='BOULK@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BOUMW', aanhef='dhr.', naam='W. Bouma, BSc', postvaknummer=96, email='BOUMW@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BOUSA', aanhef='dhr.', naam='A. Boussaboun', postvaknummer=103, email='BOUSA@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BOUSD', aanhef='dhr.', naam='D. Boussatta', postvaknummer=110, email='BOUSD@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BOUSM', aanhef='dhr.', naam='M. Boussoufa', postvaknummer=117, email='BOUSM@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BOUTS', aanhef='dhr. drs.', naam='S. Boutahar', postvaknummer=3, email='BOUTS@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BRAAE', aanhef='dhr.', naam='E.T. Braafheid, MSc', postvaknummer=10, email='BRAAE@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BRAAU', aanhef='dhr.', naam='U.R.L. te Braak', postvaknummer=17, email='BRAAU@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BRATH', aanhef='mw. drs.', naam='Th. Brack', postvaknummer=24, email='BRATH@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BRAMW', aanhef='dhr. ir.', naam='W. Brama', postvaknummer=31, email='BRAMW@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BRANM', aanhef='dhr.', naam='M. Brands', postvaknummer=38, email='BRANM@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BRANE', aanhef='dhr.', naam='E. Brandts', postvaknummer=45, email='BRANE@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BRAZB', aanhef='dhr.', naam='B. Brazil', postvaknummer=52, email='BRAZB@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BREDJ', aanhef='mw. drs.', naam='J. van Breda Kolff', postvaknummer=59, email='BREDJ@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BREEN', aanhef='dhr. ir.', naam='N. de Bree', postvaknummer=66, email='BREEN@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BREIR', aanhef='dhr.', naam='R. Breinburg', postvaknummer=73, email='BREIR@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BREUM', aanhef='dhr.', naam='M. Breuer', postvaknummer=80, email='BREUM@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BREUH', aanhef='dhr.', naam='H. van Breukelen', postvaknummer=87, email='BREUH@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BREUT', aanhef='dhr.', naam='T. Breukers', postvaknummer=94, email='BREUT@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BRINJ', aanhef='dhr.', naam='J. ten Brinke', postvaknummer=101, email='BRINJ@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BROEB', aanhef='dhr.', naam='B. van den Broek', postvaknummer=108, email='BROEB@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BROEJ', aanhef='dhr.', naam='J. Broerse', postvaknummer=115, email='BROEJ@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BROKW', aanhef='dhr.', naam='W.W. Brokamp', postvaknummer=1, email='BROKW@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BROMJ', aanhef='dhr.', naam='J. van den Brom', postvaknummer=8, email='BROMJ@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BRONG', aanhef='dhr. drs.', naam='G. van Bronckhorst', postvaknummer=15, email='BRONG@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BRUGA', aanhef='dhr.', naam='A. Bruggink', postvaknummer=22, email='BRUGA@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BRUIJ', aanhef='mw.', naam='J. Bruin', postvaknummer=29, email='BRUIJ@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BRUIL', aanhef='mw. drs.', naam='L. Bruins', postvaknummer=36, email='BRUIL@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BRUMJ', aanhef='mw. drs.', naam='J. Bruma', postvaknummer=43, email='BRUMJ@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BRUMM', aanhef='dhr.', naam='M. Bruma', postvaknummer=50, email='BRUMM@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BRUSM', aanhef='dhr.', naam='M. Brusselers', postvaknummer=57, email='BRUSM@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BRUST', aanhef='dhr.', naam='T. Brusselers', postvaknummer=64, email='BRUST@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BUIJD', aanhef='dhr.', naam='D.D. Buijs, MSc', postvaknummer=71, email='BUIJD@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BUIKR', aanhef='dhr.', naam='R.E. Buikema, RA', postvaknummer=78, email='BUIKR@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BUNJI', aanhef='dhr.', naam='J.I.T. van Bun', postvaknummer=85, email='BUNJI@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BURTH', aanhef='dhr. drs.', naam='Th. van den Burch', postvaknummer=92, email='BURTH@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BURGJ', aanhef='dhr.', naam='J. Burgers', postvaknummer=99, email='BURGJ@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BURGM', aanhef='dhr.', naam='M. Burgzorg', postvaknummer=106, email='BURGM@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BURID', aanhef='mw. drs.', naam='D. van Burik', postvaknummer=113, email='BURID@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BUSDD', aanhef='dhr.', naam='D. Bus', postvaknummer=120, email='BUSDD@DKC.NL', wachtwoord='a')
            docent.put()
            docent = entities.Docent(docentID='BUSKM', aanhef='dhr.', naam='M. Buskermolen', postvaknummer=6, email='BUSKM@DKC.N', wachtwoord='a')
            docent.put()        
            self.response.out.write('Docenten toegevoegd aan de datastore')
        else:
            self.response.out.write(htmlHelper.startTable(header=['docentID','Aanhef','Naam','Postvaknummer','email', 'wachtwoord']))
            for docent in docenten:
                self.response.out.write("<tr>")
                self.response.out.write("<td>"+docent.docentID+"</td>")
                self.response.out.write("<td>"+docent.aanhef+"</td>")
                self.response.out.write("<td>"+docent.naam+"</td>")
                self.response.out.write("<td>"+str(docent.postvaknummer)+"</td>")
                self.response.out.write("<td>"+docent.email+"</td>")
                self.response.out.write("<td>"+docent.wachtwoord+"</td>")
                self.response.out.write("</tr>")
            self.response.out.write("</table>")
            self.response.out.write("<form action='/insert/docentpost' method='post'><input type='hidden' name='delete' value='delete' /><input type='submit' value='Delete All' /></form")
            self.response.out.write(htmlHelper.footer())

class InsertVak(webapp.RequestHandler):
    def get(self):
        self.response.out.write(htmlHelper.header())
        vakken = entities.Vak.all()
        if(vakken.count() == 0):
            vak = entities.Vak(vakCode='NED', vakNaam='Nederlands')
            vak.put()
            vak = entities.Vak(vakCode='ENG', vakNaam='Engels')
            vak.put()
            vak = entities.Vak(vakCode='DUI', vakNaam='Duits')
            vak.put()
            vak = entities.Vak(vakCode='FRA', vakNaam='Frans')
            vak.put()
            vak = entities.Vak(vakCode='WIS', vakNaam='Wiskunde')
            vak.put()
            vak = entities.Vak(vakCode='INF', vakNaam='Informatica')
            vak.put()
            vak = entities.Vak(vakCode='BIO', vakNaam='Biologie')
            vak.put()
            vak = entities.Vak(vakCode='SCH', vakNaam='Scheikunde')
            vak.put()
            vak = entities.Vak(vakCode='NAT', vakNaam='Natuurkunde')
            vak.put()
            vak = entities.Vak(vakCode='GES', vakNaam='Geschiedenins')
            vak.put()
            vak = entities.Vak(vakCode='AAR', vakNaam='Aardrijkskunde')
            vak.put()
            vak = entities.Vak(vakCode='ECO', vakNaam='Economi')
            vak.put()
            
            self.response.out.write('Vakken toegevoegd aan de datastore')
        else:
            self.response.out.write(htmlHelper.startTable(header=['VakCode','VakNaam']))
            for vak in vakken:
                self.response.out.write("<tr>")
                self.response.out.write("<td>"+vak.vakCode+"</td>")
                self.response.out.write("<td>"+vak.vakNaam+"</td>")
                self.response.out.write("</tr>")
            self.response.out.write("</table>")
            self.response.out.write("<form action='/insert/vakpost' method='post'><input type='hidden' name='delete' value='delete' /><input type='submit' value='Delete All' /></form")
            self.response.out.write(htmlHelper.footer())

class InsertVakPerKlas(webapp.RequestHandler):
    def get(self):
        self.response.out.write(htmlHelper.header())
        vakken = entities.VakPerKlas.all()
        if(vakken.count() == 0):
            vak = entities.VakPerKlas(jaargang='2010-2011', klas='h3', vakCode='NED', docentID='BAARR')
            vak.put()
            vak = entities.VakPerKlas(jaargang='2010-2011', klas='h3', vakCode='ENG', docentID='BABER')
            vak.put()
            vak = entities.VakPerKlas(jaargang='2010-2011', klas='h3', vakCode='DUI', docentID='BACUL')
            vak.put()
            vak = entities.VakPerKlas(jaargang='2010-2011', klas='h3', vakCode='FRA', docentID='BAKAX')
            vak.put()
            vak = entities.VakPerKlas(jaargang='2010-2011', klas='h3', vakCode='WIS', docentID='BAKET')
            vak.put()
            self.response.out.write('Vakken per klas toegevoegd aan de datastore')
        else:
            self.response.out.write(htmlHelper.startTable(header=['Jaargang','Klas','VakCode','docentID']))
            for vak in vakken:
                self.response.out.write("<tr>")
                self.response.out.write("<td>"+vak.jaargang+"</td>")
                self.response.out.write("<td>"+vak.klas+"</td>")
                self.response.out.write("<td>"+vak.vakCode+"</td>")
                self.response.out.write("<td>"+vak.docentID+"</td>")
                self.response.out.write("</tr>")
            self.response.out.write("</table>")
            self.response.out.write("<form action='/insert/vakpost' method='post'><input type='hidden' name='delete' value='delete' /><input type='submit' value='Delete All' /></form")
            self.response.out.write(htmlHelper.footer())


class PostAfspraak(webapp.RequestHandler):
    def post(self):
        if(self.request.get('delete') == 'delete'):
            afspraken = db.GqlQuery("SELECT * FROM Afspraak")
            for afspraak in afspraken:
                afspraak.delete()
            self.response.out.write(htmlHelper.header())
            self.response.out.write("<p>Deleted all entries <a href='/insert/afspraak'>terug (insert nieuwe data)</a></p></body></html>")
            self.response.out.write(htmlHelper.footer())

class PostDocent(webapp.RequestHandler):
    def post(self):
        if(self.request.get('delete') == 'delete'):
            docenten = db.GqlQuery("SELECT * FROM Docent")
            for docent in docenten:
                docent.delete()
            self.response.out.write(htmlHelper.header())
            self.response.out.write("<p>Deleted all entries <a href='/insert/docent'>terug (insert nieuwe data)</a></p></body></html>")
            self.response.out.write(htmlHelper.footer())

class PostVak(webapp.RequestHandler):
    def post(self):
        if(self.request.get('delete') == 'delete'):
            vakken = db.GqlQuery("SELECT * FROM Vak")
            for vak in vakken:
                vak.delete()
            self.response.out.write(htmlHelper.header())
            self.response.out.write("<p>Deleted all entries <a href='/insert/vak'>terug (insert nieuwe data)</a></p></body></html>")
            self.response.out.write(htmlHelper.footer())

class PostVakPerKlas(webapp.RequestHandler):
    def post(self):
        if(self.request.get('delete') == 'delete'):
            vakken = db.GqlQuery("SELECT * FROM VakPerKlas")
            for vak in vakken:
                vak.delete()
            self.response.out.write(htmlHelper.header())
            self.response.out.write("<p>Deleted all entries <a href='/insert/vakperklas'>terug (insert nieuwe data)</a></p></body></html>")
            self.response.out.write(htmlHelper.footer())


def main():
    application = webapp.WSGIApplication([('/insert/afspraak', InsertAfspraak), 
                                          ('/insert/afspraakpost', PostAfspraak),
                                          ('/insert/docent', InsertDocent),
                                          ('/insert/docentpost', PostDocent),
                                          ('/insert/vak', InsertVak),
                                          ('/insert/vakpost', PostVak),
                                          ('/insert/vakperklas', InsertVakPerKlas),
                                          ('/insert/vakperklaspost', PostVakPerKlas),
                                          ('/insert', InsertRoot)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
