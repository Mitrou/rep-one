class Ticket:

    def is_lucky(self):
        t_t = 'Its lucky ticket. Eat it immediately!'
        t_f = 'Nope its not. Better luck next time.'
        n_v = 'Its not a valid ticked number'
        p1 = 0
        p2 = 0
        if self.isdecimal() is True and self.index(self[-1]) == 5:
            for i in self[:3]:
                p1 = p1 + int(i)
            for i in self[3:]:
                p2 = p2 + int(i)
            if p1 == p2:
                return t_t
            else:
                return t_f
        else:
            return n_v


print(Ticket.is_lucky(input('whats your ticked ID?')))
