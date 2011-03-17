# __BEGIN_LICENSE__
# Copyright (C) 2008-2010 United States Government as represented by
# the Administrator of the National Aeronautics and Space Administration.
# All Rights Reserved.
# __END_LICENSE__

from django.test import TestCase
from django.contrib.auth.models import User

class GeocamTalkUnitTest(TestCase):
    fixtures = ['demoTalkMessages.json', 'demoUsers.json']
    
    def setUp(self):
        self.now = datetime.now()
    
    def testEnsureRecipientsCanBeAddedToAMessage(self):
        # arrange
        sender = User.objects.all()[0]
        recipienta = User.objects.all()[1]
        recipientb = User.objects.all()[2]

        # act
        message = MemoMessage.objects.create(
            content="012345678901234567890123456789", 
            content_timestamp=self.now, 
            author=sender, 
            recipients = [recipienta, recipientb])
        
        # assert
        self.assertEquals(2, len(message.recipients), "All recipients should be added to the message")