class ReviewsController < ApplicationController
    before_action :set_professor

    def new
        @review = @professor.reviews.build
    end

    def create
        @review = @professor.reviews.build(review_params)
        @review.student = current_user

        if @review.save
        redirect_to professor_path(@professor), notice: 'Review created successfully.'
        else
        render :new
        end
    end

    private

    def set_professor
        @professor = Professor.find(params[:professor_id])
    end

    def review_params
        params.require(:review).permit(:content, :rating)
    end
end
