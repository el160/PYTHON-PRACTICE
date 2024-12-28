#to sort querysets django uses order_by() method
# by default it sorts in ascending order
# eg  mydata = player.objects.all().order_by('firstname').values()


# to sort in descending order use -fieldname
# eg mydata = player.objects.all().order_by('-firstname').values()


# to sort by multiple fields use  a comma order_by('field1','field2')
# eg mydata = player.objects.all().order_by('firstname','lastname').values()