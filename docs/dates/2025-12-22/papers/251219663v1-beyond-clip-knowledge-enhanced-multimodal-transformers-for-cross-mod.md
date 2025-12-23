---
layout: default
title: Beyond CLIP: Knowledge-Enhanced Multimodal Transformers for Cross-Modal Alignment in Diabetic Retinopathy Diagnosis
---

# Beyond CLIP: Knowledge-Enhanced Multimodal Transformers for Cross-Modal Alignment in Diabetic Retinopathy Diagnosis
**arXiv**：[2512.19663v1](https://arxiv.org/abs/2512.19663) · [PDF](https://arxiv.org/pdf/2512.19663.pdf)  
**作者**：Argha Kamal Samanta, Harshika Goyal, Vasudha Joshi, Tushar Mungle, Pabitra Mitra  

**一句话要点**：提出知识增强多模态Transformer框架，以解决糖尿病视网膜病变诊断中的跨模态对齐问题。

**关键词**：糖尿病视网膜病变诊断, 跨模态对齐, 多模态Transformer, 知识增强嵌入, 医学图像检索, 零样本评估

## 3 点简述
- 核心问题：通用视觉语言模型在医学领域跨模态检索中表现不佳，尤其在眼科图像与文本对齐方面存在差距。
- 方法要点：集成视网膜图像、临床文本和结构化数据，通过多模态Transformer架构和多种损失函数进行联合训练。
- 实验或效果：在BRSET数据集上实现近完美的检索性能，并在DeepEyeNet上验证了强泛化能力，同时保持高分类准确率。

## 摘要（原文）

> Diabetic retinopathy (DR) is a leading cause of preventable blindness worldwide, demanding accurate automated diagnostic systems. While general-domain vision-language models like Contrastive Language-Image Pre-Training (CLIP) perform well on natural image tasks, they struggle in medical domain applications, particularly in cross-modal retrieval for ophthalmological images. We propose a novel knowledge-enhanced joint embedding framework that integrates retinal fundus images, clinical text, and structured patient data through a multimodal transformer architecture to address the critical gap in medical image-text alignment. Our approach employs separate encoders for each modality: a Vision Transformer (ViT-B/16) for retinal images, Bio-ClinicalBERT for clinical narratives, and a multilayer perceptron for structured demographic and clinical features. These modalities are fused through a joint transformer with modality-specific embeddings, trained using multiple objectives including contrastive losses between modality pairs, reconstruction losses for images and text, and classification losses for DR severity grading according to ICDR and SDRG schemes. Experimental results on the Brazilian Multilabel Ophthalmological Dataset (BRSET) demonstrate significant improvements over baseline models. Our framework achieves near-perfect text-to-image retrieval performance with Recall@1 of 99.94% compared to fine-tuned CLIP's 1.29%, while maintaining state-of-the-art classification accuracy of 97.05% for SDRG and 97.97% for ICDR. Furthermore, zero-shot evaluation on the unseen DeepEyeNet dataset validates strong generalizability with 93.95% Recall@1 versus 0.22% for fine-tuned CLIP. These results demonstrate that our multimodal training approach effectively captures cross-modal relationships in the medical domain, establishing both superior retrieval capabilities and robust diagnostic performance.

