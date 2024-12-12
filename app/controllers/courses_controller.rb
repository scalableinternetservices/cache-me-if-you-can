class CoursesController < ApplicationController
  def index
    @page = (params[:page] || 1).to_i
    @per_page = 50 # Number of courses per page
    if params[:search].present?
      @courses = Course.where("name ILIKE ? OR code ILIKE ?", "%#{params[:search]}%", "%#{params[:search]}%")
    else
      @courses = Course.all
    end

    @total_pages = (@courses.count / @per_page.to_f).ceil
    if @total_pages == 0
      @total_pages = 1
    end
    @courses = @courses.offset((@page - 1) * @per_page).limit(@per_page)

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
  