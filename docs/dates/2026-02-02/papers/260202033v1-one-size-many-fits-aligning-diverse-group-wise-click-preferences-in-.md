---
layout: default
title: One Size, Many Fits: Aligning Diverse Group-Wise Click Preferences in Large-Scale Advertising Image Generation
---

# One Size, Many Fits: Aligning Diverse Group-Wise Click Preferences in Large-Scale Advertising Image Generation
**arXiv**：[2602.02033v1](https://arxiv.org/abs/2602.02033) · [PDF](https://arxiv.org/pdf/2602.02033.pdf)  
**作者**：Shuo Lu, Haohan Wang, Wei Feng, Weizhen Wang, Shen Zhang, Yaoyu Li, Ao Ma, Zheng Zhang, Jingjing Lv, Junjie Shen, Ching Law, Bing Zhan, Yuan Xu, Huizai Yao, Yongcan Yu, Chenyang Si, Jian Liang  

**一句话要点**：提出OSMF框架以解决广告图像生成中用户群体偏好多样性的对齐问题

**关键词**：广告图像生成, 群体偏好对齐, 多模态大语言模型, 点击率优化, 自适应分组, 偏好数据集

## 3 点简述
- 核心问题：现有方法采用‘一刀切’策略优化整体点击率，忽视用户群体偏好差异，导致特定群体效果不佳
- 方法要点：通过产品感知自适应分组和基于G-MLLM的偏好条件图像生成，结合Group-DPO微调实现群体偏好对齐
- 实验或效果：在离线与在线实验中达到最先进性能，并发布首个大规模群体图像偏好数据集GAIP

## 摘要（原文）

> Advertising image generation has increasingly focused on online metrics like Click-Through Rate (CTR), yet existing approaches adopt a ``one-size-fits-all" strategy that optimizes for overall CTR while neglecting preference diversity among user groups. This leads to suboptimal performance for specific groups, limiting targeted marketing effectiveness. To bridge this gap, we present \textit{One Size, Many Fits} (OSMF), a unified framework that aligns diverse group-wise click preferences in large-scale advertising image generation. OSMF begins with product-aware adaptive grouping, which dynamically organizes users based on their attributes and product characteristics, representing each group with rich collective preference features. Building on these groups, preference-conditioned image generation employs a Group-aware Multimodal Large Language Model (G-MLLM) to generate tailored images for each group. The G-MLLM is pre-trained to simultaneously comprehend group features and generate advertising images. Subsequently, we fine-tune the G-MLLM using our proposed Group-DPO for group-wise preference alignment, which effectively enhances each group's CTR on the generated images. To further advance this field, we introduce the Grouped Advertising Image Preference Dataset (GAIP), the first large-scale public dataset of group-wise image preferences, including around 600K groups built from 40M users. Extensive experiments demonstrate that our framework achieves the state-of-the-art performance in both offline and online settings. Our code and datasets will be released at https://github.com/JD-GenX/OSMF.

