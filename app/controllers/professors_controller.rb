class ProfessorsController < ApplicationController
  before_action :show_user, only: [:index, :search]
    def index
      @page = (params[:page] || 1).to_i
      @per_page = 10 # Number of professors per page
      @total_pages = (Professor.count / @per_page.to_f).ceil
      @professors = Professor.offset((@page - 1) * @per_page).limit(@per_page)
    end
  
    def show
      @professor = Professor.find(params[:id])
      @rating_calculation_reviews = @professor.reviews
      @courses = @professor.courses.distinct.order(:name)

      if params[:course_id].present?
        @selected_course = Course.find(params[:course_id])
        @reviews = @professor.reviews.where(course: @selected_course)
        @rating_calculation_reviews = @professor.reviews.where(course_id: params[:course_id])
      else
        @selected_course = nil
        @reviews = @professor.reviews
      end


      if @rating_calculation_reviews.any?
        aggregate_rating = @rating_calculation_reviews.sum(:rating)
        count = @rating_calculation_reviews.count
        @average_rating = (aggregate_rating.to_f / count).round(2)
      else
        @average_rating = nil
      end
    end
  
    def new
      @professor = Professor.new
    end
  
    def create
      @professor = Professor.new(professor_params)
      if @professor.save
        redirect_to professors_path, notice: 'Professor was successfully created.'
      else
        render :new
      end
    end

    def search
      @page = (params[:page] || 1).to_i
      @per_page = 10 # Number of professors per page

      if params[:query].present? and params[:query].length > 0
        @professors = Professor.where("name LIKE ?", "%#{params[:query]}%")
      else
        @professors = Professor.all
      end

      @total_pages = (@professors.size / @per_page.to_f).ceil
      @professors = @professors.offset((@page - 1) * @per_page).limit(@per_page)

      render :index
    end
  
    private
  
    def professor_params
      params.require(:professor).permit(:name, :department)
    end

    def show_user
      @current_user = Student.find_by(id: session[:student_id]) if session[:student_id]
    end
  end
  