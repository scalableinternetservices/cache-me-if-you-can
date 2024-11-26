class CoursesController < ApplicationController
  def index
    if params[:search].present?
      @courses = Course.where("name ILIKE ? OR code ILIKE ?", "%#{params[:search]}%", "%#{params[:search]}%")
    else
      @courses = Course.all
    end
  end
    def new
      @course = Course.new
      @professors = Professor.all  # Load all professors for the dropdown
    end
  
    def create
      @course = Course.new(course_params)
      if @course.save
        redirect_to courses_path, notice: "Course was successfully created."
      else
        render :new
      end
    end

    def show
      @course = Course.find(params[:id])
      @professors = @course.professors  # Fetches all professors associated with the course
    end

    private
  
    def course_params
      params.require(:course).permit(:name, :code, :description)
    end
  end
  