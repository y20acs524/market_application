from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Length,Email,EqualTo,DataRequired,ValidationError
from market.models import User

class RegisterForm(FlaskForm):
    
    def validate_user_name(self,username_to_check):
        user=User.query.filter_by(user_name=username_to_check.data).first()
        if user:
            raise ValidationError("UserName already exists.Try new one!!")
        
    
    def validate_email_address(self,email_to_check):
        user=User.query.filter_by(email_address=email_to_check.data ).first()
        if user:
            raise ValidationError("Email already exists.Try new one!!")
    
    user_name=StringField(label="User Name: ", validators=[Length(min=5,max=30), DataRequired()])
    email_address=StringField(label='Email Address: ', validators=[Email(), DataRequired()])
    password1=PasswordField(label='Password: ', validators=[Length(min=6), DataRequired()])
    password2=PasswordField(label='Confirm Password: ',validators=[EqualTo('password1'), DataRequired()])
    submit=SubmitField(label='Create Account')
    
    
class LoginForm(FlaskForm):
    user_name=StringField(label="User Name: ",validators=[DataRequired()])
    password=PasswordField(label="password: ",validators=[DataRequired()])
    submit=SubmitField(label="signin")
    
class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label="Purchase Item")
    
class SellItemForm(FlaskForm):
    submit = SubmitField(label="Sell Item")