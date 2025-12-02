---
layout: default
title: FlashVGGT: Efficient and Scalable Visual Geometry Transformers with Compressed Descriptor Attention
---

# FlashVGGT: Efficient and Scalable Visual Geometry Transformers with Compressed Descriptor Attention
**arXiv**：[2512.01540v1](https://arxiv.org/abs/2512.01540) · [PDF](https://arxiv.org/pdf/2512.01540.pdf)  
**作者**：Zipeng Wang, Dan Xu  

**一句话要点**：提出FlashVGGT以解决多视图3D重建中自注意力二次复杂度导致的扩展性问题

**关键词**：多视图3D重建, 描述符注意力, 长序列处理, 计算效率优化, 视觉几何变换器

## 3 点简述
- 核心问题：VGGT等模型因全自注意力二次复杂度，在处理长图像序列时扩展性差
- 方法要点：通过压缩空间信息为描述符令牌，采用描述符注意力机制替代密集全局注意力
- 实验或效果：在1000张图像上推理时间降至VGGT的9.3%，可扩展至超过3000张图像

## 摘要（原文）

> 3D reconstruction from multi-view images is a core challenge in computer vision. Recently, feed-forward methods have emerged as efficient and robust alternatives to traditional per-scene optimization techniques. Among them, state-of-the-art models like the Visual Geometry Grounding Transformer (VGGT) leverage full self-attention over all image tokens to capture global relationships. However, this approach suffers from poor scalability due to the quadratic complexity of self-attention and the large number of tokens generated in long image sequences. In this work, we introduce FlashVGGT, an efficient alternative that addresses this bottleneck through a descriptor-based attention mechanism. Instead of applying dense global attention across all tokens, FlashVGGT compresses spatial information from each frame into a compact set of descriptor tokens. Global attention is then computed as cross-attention between the full set of image tokens and this smaller descriptor set, significantly reducing computational overhead. Moreover, the compactness of the descriptors enables online inference over long sequences via a chunk-recursive mechanism that reuses cached descriptors from previous chunks. Experimental results show that FlashVGGT achieves reconstruction accuracy competitive with VGGT while reducing inference time to just 9.3% of VGGT for 1,000 images, and scaling efficiently to sequences exceeding 3,000 images. Our project page is available at https://wzpscott.github.io/flashvggt_page/.

