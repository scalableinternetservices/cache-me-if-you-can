class CommentsController < ApplicationController
    def create
        @review = Review.find(params[:review_id])
        @comment = @review.comments.build(comment_params)
        @comment.student = current_student if current_student
        
        if @comment.save
            redirect_to professor_reviews_path(@review.professor, @review), notice: "Comment added."
        else
            redirect_to professor_reviews_path(@review.professor, @review), alert: @comment.errors.full_messages.to_sentence
        end
    end

    private

    def comment_params
        params.require(:comment).permit(:content)
    end
end
