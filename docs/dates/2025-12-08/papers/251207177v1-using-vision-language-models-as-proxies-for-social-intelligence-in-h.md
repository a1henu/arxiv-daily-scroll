---
layout: default
title: Using Vision-Language Models as Proxies for Social Intelligence in Human-Robot Interaction
---

# Using Vision-Language Models as Proxies for Social Intelligence in Human-Robot Interaction
**arXiv**：[2512.07177v1](https://arxiv.org/abs/2512.07177) · [PDF](https://arxiv.org/pdf/2512.07177.pdf)  
**作者**：Fanjun Bu, Melina Tsai, Audrey Tjokro, Tapomayukh Bhattacharjee, Jorge Ortiz, Wendy Ju  

**一句话要点**：提出两阶段视觉语言模型代理方法，以提升机器人在日常环境中基于非语言线索的社交互动决策能力。

**关键词**：人机交互, 视觉语言模型, 非语言线索, 社交机器人, 选择性触发, 现场部署

## 3 点简述
- 核心问题：机器人在日常环境中需基于微妙非语言线索决定是否与人互动，但此类线索难以显式建模。
- 方法要点：结合轻量感知检测器与视觉语言模型，在社交关键时刻选择性触发视频查询，实现社交推理代理。
- 实验或效果：通过回放现场交互评估，验证方法能促进机器人社交响应行为，使其更自然地关注现实互动中的线索。

## 摘要（原文）

> Robots operating in everyday environments must often decide when and whether to engage with people, yet such decisions often hinge on subtle nonverbal cues that unfold over time and are difficult to model explicitly. Drawing on a five-day Wizard-of-Oz deployment of a mobile service robot in a university cafe, we analyze how people signal interaction readiness through nonverbal behaviors and how expert wizards use these cues to guide engagement. Motivated by these observations, we propose a two-stage pipeline in which lightweight perceptual detectors (gaze shifts and proxemics) are used to selectively trigger heavier video-based vision-language model (VLM) queries at socially meaningful moments. We evaluate this pipeline on replayed field interactions and compare two prompting strategies. Our findings suggest that selectively using VLMs as proxies for social reasoning enables socially responsive robot behavior, allowing robots to act appropriately by attending to the cues people naturally provide in real-world interactions.

