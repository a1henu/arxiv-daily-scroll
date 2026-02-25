---
layout: default
title: AnimeAgent: Is the Multi-Agent via Image-to-Video models a Good Disney Storytelling Artist?
---

# AnimeAgent: Is the Multi-Agent via Image-to-Video models a Good Disney Storytelling Artist?
**arXiv**：[2602.20664v1](https://arxiv.org/abs/2602.20664) · [PDF](https://arxiv.org/pdf/2602.20664.pdf)  
**作者**：Hailong Yan, Shice Liu, Tao Wang, Xiangtao Zhang, Yijie Zhong, Jinwei Chen, Le Zhang, Bo Li  

**一句话要点**：提出AnimeAgent，首个基于图像到视频的多智能体框架，用于定制故事板生成以解决动态表达和一致性不足问题。

**关键词**：定制故事板生成, 图像到视频模型, 多智能体框架, 动画一致性, 迭代优化, 风格化评估

## 3 点简述
- 核心问题：现有静态扩散模型在定制故事板生成中缺乏动态表达，依赖复制粘贴模式，且多智能体评估不适用于风格化动画。
- 方法要点：利用图像到视频模型的隐式运动先验增强一致性，结合混合主观-客观评审器实现迭代优化，灵感来自迪士尼动画工作流。
- 实验或效果：在收集的人类标注基准上，AnimeAgent在一致性、提示忠实度和风格化方面达到最先进性能。

## 摘要（原文）

> Custom Storyboard Generation (CSG) aims to produce high-quality, multi-character consistent storytelling. Current approaches based on static diffusion models, whether used in a one-shot manner or within multi-agent frameworks, face three key limitations: (1) Static models lack dynamic expressiveness and often resort to "copy-paste" pattern. (2) One-shot inference cannot iteratively correct missing attributes or poor prompt adherence. (3) Multi-agents rely on non-robust evaluators, ill-suited for assessing stylized, non-realistic animation. To address these, we propose AnimeAgent, the first Image-to-Video (I2V)-based multi-agent framework for CSG. Inspired by Disney's "Combination of Straight Ahead and Pose to Pose" workflow, AnimeAgent leverages I2V's implicit motion prior to enhance consistency and expressiveness, while a mixed subjective-objective reviewer enables reliable iterative refinement. We also collect a human-annotated CSG benchmark with ground-truth. Experiments show AnimeAgent achieves SOTA performance in consistency, prompt fidelity, and stylization.

