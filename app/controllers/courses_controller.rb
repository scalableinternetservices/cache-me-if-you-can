class CoursesController < ApplicationController
    def new
      @course = Course.new
      @professors = Professor.all  # Load all professors for the dropdown
    end
  
    def create
      @course = Course.new(course_params)
      if @course.save
        redirect_to professors_path, notice: "Course was successfully created."
      else
        render :new
      end
    end
  
    private
  
    def course_params
      params.require(:course).permit(:name, :code, :description, :professor_id)
    end
  end
  