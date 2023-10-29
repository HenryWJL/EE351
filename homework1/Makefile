.PHONY : demo

define sort_file
	@du * -sh|sort -h
endef

define find_log
	@find -name *.log
endef

define delete_lock_file
	@find -name *.lock | xargs rm -r
endef

demo:
	$(call sort_file)
	$(call find_log)
	$(call delete_lock_file)
