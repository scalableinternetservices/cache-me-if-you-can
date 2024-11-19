class ApplicationController < ActionController::Base
  skip_before_action :verify_authenticity_token
  
  helper_method :current_student

  def current_student
    @current_student ||= Student.find_by(id: session[:student_id]) if session[:student_id]
  end
end
