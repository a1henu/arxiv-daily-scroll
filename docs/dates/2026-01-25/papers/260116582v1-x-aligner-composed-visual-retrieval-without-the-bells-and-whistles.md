---
layout: default
title: X-Aligner: Composed Visual Retrieval without the Bells and Whistles
---

# X-Aligner: Composed Visual Retrieval without the Bells and Whistles
**arXiv**：[2601.16582v1](https://arxiv.org/abs/2601.16582) · [PDF](https://arxiv.org/pdf/2601.16582.pdf)  
**作者**：Yuqian Zheng, Mariana-Iuliana Georgescu  

**一句话要点**：提出X-Aligner框架以解决组合视频检索中多模态融合不足的问题

**关键词**：组合视频检索, 跨注意力模块, 视觉语言模型, 零样本泛化, 多模态融合

## 3 点简述
- 现有组合视频检索框架单阶段融合多模态输入，性能提升有限
- 引入跨注意力模块X-Aligner，渐进融合视觉与文本查询并对齐目标视频表示
- 在Webvid-CoVR数据集上训练，实现63.93%的Recall@1，并在CIR任务中展示零样本泛化能力

## 摘要（原文）

> Composed Video Retrieval (CoVR) facilitates video retrieval by combining visual and textual queries. However, existing CoVR frameworks typically fuse multimodal inputs in a single stage, achieving only marginal gains over initial baseline. To address this, we propose a novel CoVR framework that leverages the representational power of Vision Language Models (VLMs). Our framework incorporates a novel cross-attention module X-Aligner, composed of cross-attention layers that progressively fuse visual and textual inputs and align their multimodal representation with that of the target video. To further enhance the representation of the multimodal query, we incorporate the caption of the visual query as an additional input. The framework is trained in two stages to preserve the pretrained VLM representation. In the first stage, only the newly introduced module is trained, while in the second stage, the textual query encoder is also fine-tuned. We implement our framework on top of BLIP-family architecture, namely BLIP and BLIP-2, and train it on the Webvid-CoVR data set. In addition to in-domain evaluation on Webvid-CoVR-Test, we perform zero-shot evaluations on the Composed Image Retrieval (CIR) data sets CIRCO and Fashion-IQ. Our framework achieves state-of-the-art performance on CoVR obtaining a Recall@1 of 63.93% on Webvid-CoVR-Test, and demonstrates strong zero-shot generalization on CIR tasks.

