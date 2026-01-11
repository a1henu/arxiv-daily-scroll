---
layout: default
title: From Understanding to Engagement: Personalized pharmacy Video Clips via Vision Language Models (VLMs)
---

# From Understanding to Engagement: Personalized pharmacy Video Clips via Vision Language Models (VLMs)
**arXiv**：[2601.05059v1](https://arxiv.org/abs/2601.05059) · [PDF](https://arxiv.org/pdf/2601.05059.pdf)  
**作者**：Suyash Mishra, Qiang Li, Srikanth Patil, Anubhav Girdhar  

**一句话要点**：提出基于VLM和ALM的个性化药学长视频剪辑框架，以解决多模态内容处理效率低和质量不一致问题。

**关键词**：视频剪辑生成, 多模态处理, 个性化提示, 药学长视频, 成本效率优化

## 3 点简述
- 核心问题：传统手动标注多模态数据（如长视频）效率低、质量差，阻碍药企数字化转型。
- 方法要点：结合Cut & Merge算法和角色定义提示注入，实现平滑剪辑与个性化输出（如营销、培训）。
- 实验或效果：在Video MME和专有数据集上验证，速度提升3-4倍，成本降低4倍，剪辑质量优于基线VLM。

## 摘要（原文）

> Vision Language Models (VLMs) are poised to revolutionize the digital transformation of pharmacyceutical industry by enabling intelligent, scalable, and automated multi-modality content processing. Traditional manual annotation of heterogeneous data modalities (text, images, video, audio, and web links), is prone to inconsistencies, quality degradation, and inefficiencies in content utilization. The sheer volume of long video and audio data further exacerbates these challenges, (e.g. long clinical trial interviews and educational seminars).
>   Here, we introduce a domain adapted Video to Video Clip Generation framework that integrates Audio Language Models (ALMs) and Vision Language Models (VLMs) to produce highlight clips. Our contributions are threefold: (i) a reproducible Cut & Merge algorithm with fade in/out and timestamp normalization, ensuring smooth transitions and audio/visual alignment; (ii) a personalization mechanism based on role definition and prompt injection for tailored outputs (marketing, training, regulatory); (iii) a cost efficient e2e pipeline strategy balancing ALM/VLM enhanced processing. Evaluations on Video MME benchmark (900) and our proprietary dataset of 16,159 pharmacy videos across 14 disease areas demonstrate 3 to 4 times speedup, 4 times cost reduction, and competitive clip quality. Beyond efficiency gains, we also report our methods improved clip coherence scores (0.348) and informativeness scores (0.721) over state of the art VLM baselines (e.g., Gemini 2.5 Pro), highlighting the potential of transparent, custom extractive, and compliance supporting video summarization for life sciences.

