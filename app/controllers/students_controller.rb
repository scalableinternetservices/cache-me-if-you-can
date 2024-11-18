class StudentsController < ApplicationController
    def new
      @student = Student.new
    end
  
    def create
      @student = Student.new(student_params)
      if @student.save
        redirect_to login_path, notice: "Successfully registered. Please log in."
      else
        flash.alert = @student.errors.full_messages.to_sentence
        render :new, status: :unprocessable_entity
      end
    end
  
    private
  
    def student_params
      params.require(:student).permit(:username, :password)
    end
  end
  