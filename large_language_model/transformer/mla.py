# TODO(hao): implement the multi-head attention calculation from scratch.  further: gqa, mla
# https://medium.com/@zaiinn440/mha-vs-mqa-vs-gqa-vs-mla-c6cf8285bbec
# from the medium blog above, summary:
# mha: the most commonly used, while general, the huge kv cache is a problem
# gqa: grouped query attention, reduce kv cache by reducing the head num.
# mla: multi-head latent attention, reduce kv cache by compressing the kv cache into a low-dimensional latent vector. 