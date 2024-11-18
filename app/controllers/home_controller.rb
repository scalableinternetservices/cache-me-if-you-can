class HomeController < ApplicationController
  def index
    @current_user = Student.find_by(id: session[:student_id]) if session[:student_id]
  end

  def search
    @results = []
    render :searchß
  end
end
