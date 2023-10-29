.PHONY : demo

define sort_file
	@du * -sh|sort -h
endef

define find_log
	@ls ~/python/*.log
endef

define delete_lock_file
	@ls ~/python/*.lock | xargs rm -r
endef

demo:
	$(call sort_file)
	$(call find_log)
	$(call delete_lock_file)