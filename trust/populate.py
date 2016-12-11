import os

def populate():
    #add Cause objects
    edu = add_Cause(cause_id = 'ab123',
                    name = 'Education',
                    total_amount = 200000)
    hyg = add_Cause(cause_id = 'def456',
                    name = 'Hygiene',
                    total_amount = 8000)
    ill = add_Cause(cause_id = 'ghi789',
                    name = 'Illness',
                    total_amount = 87887)

    #add Project objects
    add_Project(project_id = '1212nkmk',
                title = 'abc',
                start_date = '2012-12-12',
                end_date = '2013-12-16',
                total_amount = 2000,
                raised_amount = 1000,
                cause = edu,
                ngo_id = 1,
                zip = 123456,
                person_of_contact = 'Arjun',
                summary = 'xyz',
                team_member_id = 123)
    add_Project(project_id = '23huh',
                title='efg',
                start_date='2001-1-12',
                end_date='2013-10-16',
                total_amount=5000,
                raised_amount=9000,
                cause=hyg,
                ngo_id=2,
                zip=123656,
                person_of_contact='Nikhil',
                summary='xyz',
                team_member_id=173)
    add_Project(project_id = '232njkl',
                title='hij',
                start_date='2001-12-12',
                end_date='2010-12-16',
                total_amount=7000,
                raised_amount=5000,
                cause=ill,
                ngo_id=3,
                zip=129856,
                person_of_contact='Arjun',
                summary='xyz',
                team_member_id=923)

    #add NGO objects
    add_NGO(ngo_id = '2323dff',
            name = 'shiksha',
            person_of_contact = 'Ram',
            registration_code = 78787,
            address = 'yuwyeuyew',
            website = 'www.dbfh.com',
            team_member_id = 923,)
    add_NGO(ngo_id = '2323jij',
            name='rural',
            person_of_contact='Sham',
            registration_code= 8787,
            address='weuyihdw',
            website='www.pkp.com',
            team_member_id=54545, )
    add_NGO(ngo_id = '2323kjk',
            name='fish',
            person_of_contact='Kaka',
            registration_code=4959,
            address='wuduudh',
            website='www.plpo.com',
            team_member_id=6565,)

    #add Consultant objects
    add_Consultant(consultant_id = '23938hjh',
                   name = 'Shikhar')
    add_Consultant(consultant_id = '213jjn',
                   name='Mukul')
    add_Consultant(consultant_id = '2332nj',
                   name='Jay')

    #add Audit objects
    add_Audit(audit_id = '23jbj',
              date = '2024-2-12',
              report_id = 4554,
              consultant_id = 9843989 ,
              project_id = 94834,)
    add_Audit(audit_id = '12njnj',
              date='2013-3-16',
              report_id=5454,
              consultant_id=2365265,
              project_id=3763476, )
    add_Audit(audit_id = '3223bjn',
              date='2023-12-15',
              report_id=8754,
              consultant_id=97863,
              project_id=3487, )

    #add Team_Member objects
    add_Team_Member(team_member_id = '1221dsd',
                    name = 'A')
    add_Team_Member(team_member_id = '123jhun',
                    name='B')
    add_Team_Member(team_member_id = '28723bj',
                    name='C')

    #add Donor objects
    add_Donor(donor_id = '2132nj',
              name = 'Ram',
              mobile=46544545,
              email = 'dsj@dsj.com',
              transaction_id =54515511)
    add_Donor(donor_id = '298293ds',
              name='Balram',
              mobile=784512956,
              email='sdhjh@ksjd.com',
              transaction_id=894561)
    add_Donor(donor_id = '2398329hd',
              name='Ghosh',
              mobile=844515412,
              email='iwdh@kdsn.com',
              transaction_id=96857)

    #add Donation objects
    add_Donation(transaction_id=34646,
                 donor_id=68547,
                 project_id=545,
                 amount=200,
                 date='2012-3-12',
                 time='12:13:12',)
    add_Donation(transaction_id=89451,
                 donor_id=652,
                 project_id=35132,
                 amount=400,
                 date='2023-4-15',
                 time='14:15:24',)
    add_Donation(transaction_id=8745,
                 donor_id=234,
                 project_id=545214,
                 amount=300,
                 date='2013-12-14',
                 time='18:15:18',)

def add_Cause(cause_id, name, total_amount):
    p = Cause.objects.get_or_create(cause_id = cause_id, name=name, total_amount=total_amount)[0]
    return p
def add_Project(project_id, title, start_date, end_date, total_amount, raised_amount, cause, ngo_id, zip, person_of_contact, summary, team_member_id):
    p = Project.objects.get_or_create(project_id = project_id, title = title, start_date=start_date, end_date=end_date, total_amount=total_amount, raised_amount=raised_amount, cause=cause, ngo_id=ngo_id, zip=zip, person_of_contact=person_of_contact, summary=summary, team_member_id=team_member_id)[0]
    return p
def add_NGO(ngo_id, name, person_of_contact, registration_code, address, website, team_member_id):
    p = NGO.objects.get_or_create(ngo_id = ngo_id, name=name, person_of_contact=person_of_contact, registration_code=registration_code, address=address, website=website, team_member_id=team_member_id)[0]
    return p
def add_Consultant(consultant_id, name):
    p = Consultant.objects.get_or_create(consultant_id = consultant_id, name=name,)[0]
    return p
def add_Audit(audit_id, date, report_id, consultant_id, project_id):
    p = Audit.objects.get_or_create(audit_id = audit_id, date=date, report_id=report_id, consultant_id=consultant_id, project_id=project_id)[0]
    return p
def add_Team_Member(team_member_id, name):
    p = Team_Member.objects.get_or_create(team_member_id = team_member_id, name=name)[0]
    return p
def add_Donor(donor_id, name, mobile, email, transaction_id):
    p = Donor.objects.get_or_create(donor_id = donor_id, name=name, mobile=mobile, email=email, transaction_id=transaction_id)[0]
    return p
def add_Donation(transaction_id, donor_id, project_id, amount, date, time):
    p = Donation.objects.get_or_create(transaction_id=transaction_id, donor_id=donor_id, project_id=project_id, amount=amount, date=date, time=time)[0]
    return p


#execution starts here
if __name__ == '__main__':
    print "Starting Trust population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trust.settings')
    from data.models import Cause, Project, NGO, Consultant, Audit
    from users.models import Donor, Donation
    from staff.models import Team_Member
    populate()