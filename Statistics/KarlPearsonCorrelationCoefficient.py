import math

ps = [int(x) for x in input().split()]
hs = [int(x) for x in input().split()]

ps_bar = sum(ps)/len(ps)
hs_bar = sum(hs)/len(hs)

print('ps_bar: %f' % ps_bar)
print('hs_bar: %f' % hs_bar)

num = sum(((ps[i] - ps_bar) * (hs[i] * hs_bar)) for i in range(0, len(ps)))
print('num: %f' % num)

den_ps = sum(((ps[i] - ps_bar) * (ps[i] * ps_bar)) for i in range(0, len(ps)))
print('den_ps: %f' % den_ps)

den_hs = sum(((hs[i] - hs_bar) * (hs[i] * hs_bar)) for i in range(0, len(hs)))
print('den_hs: %f' % den_hs)

den = math.sqrt(den_ps * den_hs)
print('den: %f' % den)

ans = num / den
print('Answer: %0.3f' % ans) # Printing answer upto 3 decimal places
