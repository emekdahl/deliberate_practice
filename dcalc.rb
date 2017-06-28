@my_debts = [
  {
    name: "Visa",
    current_balance: 100,
    interest_rate: 24,
    minimum_payment: 20
  },
  {
    name: "Mortgage",
    current_balance: 100,
    interest_rate: 5,
    minimum_payment: 20
  },
  {
    name: "Car",
    current_balance: 100,
    interest_rate: 7,
    minimum_payment: 20
  },
  {
    name: "Student Loan",
    current_balance: 100,
    interest_rate: 6,
    minimum_payment: 20
  },
]

@my_debts.reverse

def pay_one_month
  
  #the amount the user has to pay down debt each month
  amount = 1500
  #calculated interest variable declared
  total_interest = 0
  #total paid variable declared
  total_paid = 0
  #months counter declared
  months_counter = 0

  #loop through each debt
  @my_debts.each_with_index do |debt,index|

    #######################
    #INITIALIZING VARIABLES
    #######################
    #current balance is current balance in db
    current_balance = debt[:current_balance]
    puts current_balance.to_s
    #set interest rate to interest rate in db
    interest = debt[:interest_rate]
    #set minimum payment to minimum payment in db
    minimum_payment = debt[:minimum_payment]

    # #######################
    # #MAKING PAYMENTS
    # #######################
    
    # if current_balance < minimum_payment
    #   payment = current_balance
    # #if it is the last item in the array, payment should be whatever is left of the amount
    # elsif index ==  -1
    #   payment = amount
    # else
    # #default payment amount is minimum_payment
    #   payment = minimum_payment
    # end
    # #subtract the payment from the current balance
    # current_balance -= payment
    # # keep track of the total amount paid
    # total_paid += payment
    # # subtract the payment just made from the total amount available for payments
    # amount -= payment

    # #######################
    # #CALCULATE INTEREST
    # #######################
    # #calculate interest for debt
    # interest = current_balance * (interest/100.0/12.0)
    # puts "The interest for " + debt[:name] + " is: " + interest.to_s
    # #add this amount to total_interest
    # total_interest += interest

    # current_balance += interest
    # #make sure the new current balance for the debt is saved ?!?!?!
    # puts "The current balance for " + debt[:name] + " is: " + current_balance.to_s
    # debt[:current_balance] = current_balance
  end

end


# def total_payments
#   #add up the total current balance for all debts
#   total_current_balance = @my_debts.inject(0) {|sum,debt| sum + debt[:current_balance]}

#   #initialize a debt counter variable
#   total_months = 0

#   #keep running the pay_one_month function until @total_current_balance is zero
#   until total_current_balance <= 0 
#     #run the pay one month function
#     pay_one_month
#     #recalculate the total current balance 
#     total_current_balance = @my_debts.inject(total_current_balance) {|sum,debt| sum + debt[:current_balance]}
#     #add one to the months counter
#     total_months += 1
#   end
#   puts total_months
#   puts total_current_balance
# end

# total_payments()

