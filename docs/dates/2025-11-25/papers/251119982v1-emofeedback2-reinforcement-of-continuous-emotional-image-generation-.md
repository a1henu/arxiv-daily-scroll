---
layout: default
title: EmoFeedback2: Reinforcement of Continuous Emotional Image Generation via LVLM-based Reward and Textual Feedback
---

# EmoFeedback2: Reinforcement of Continuous Emotional Image Generation via LVLM-based Reward and Textual Feedback
**arXiv**：[2511.19982v1](https://arxiv.org/abs/2511.19982) · [PDF](https://arxiv.org/pdf/2511.19982.pdf)  
**作者**：Jingyang Jia, Kai Shu, Gang Yang, Long Xing, Xun Chen, Aiping Liu  

**一句话要点**：提出EmoFeedback2范式，通过LVLM奖励与文本反馈强化连续情感图像生成

**关键词**：连续情感图像生成, 大视觉语言模型, 强化微调, 情感奖励, 文本反馈, 情感保真度

## 3 点简述
- 现有方法缺乏情感反馈，难以控制图像情感连续性
- 利用微调LVLM提供奖励和文本反馈，增强情感连续性和保真度
- 实验显示在自定义数据集上优于现有方法，生成高质量情感图像

## 摘要（原文）

> Continuous emotional image generation (C-EICG) is emerging rapidly due to its ability to produce images aligned with both user descriptions and continuous emotional values. However, existing approaches lack emotional feedback from generated images, limiting the control of emotional continuity. Additionally, their simple alignment between emotions and naively generated texts fails to adaptively adjust emotional prompts according to image content, leading to insufficient emotional fidelity. To address these concerns, we propose a novel generation-understanding-feedback reinforcement paradigm (EmoFeedback2) for C-EICG, which exploits the reasoning capability of the fine-tuned large vision-language model (LVLM) to provide reward and textual feedback for generating high-quality images with continuous emotions. Specifically, we introduce an emotion-aware reward feedback strategy, where the LVLM evaluates the emotional values of generated images and computes the reward against target emotions, guiding the reinforcement fine-tuning of the generative model and enhancing the emotional continuity of images. Furthermore, we design a self-promotion textual feedback framework, in which the LVLM iteratively analyzes the emotional content of generated images and adaptively produces refinement suggestions for the next-round prompt, improving the emotional fidelity with fine-grained content. Extensive experimental results demonstrate that our approach effectively generates high-quality images with the desired emotions, outperforming existing state-of-the-art methods in our custom dataset. The code and dataset will be released soon.

