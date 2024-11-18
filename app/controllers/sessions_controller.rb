class SessionsController < ApplicationController
    def new
    end
  
    def create
      @student = Student.find_by(username: params[:username])
      if @student&.password == params[:password]
        session[:student_id] = @student.id
        redirect_to professors_path, notice: "Logged in successfully."
      else
        flash.alert = "Invalid username or password."
        render :new, status: :unprocessable_entity
      end
    end
  
    def destroy
      session[:student_id] = nil
      redirect_to login_path, notice: "Logged out successfully."
    end
  end
  