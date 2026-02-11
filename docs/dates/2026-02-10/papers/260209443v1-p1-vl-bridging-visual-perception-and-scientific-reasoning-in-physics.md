---
layout: default
title: P1-VL: Bridging Visual Perception and Scientific Reasoning in Physics Olympiads
---

# P1-VL: Bridging Visual Perception and Scientific Reasoning in Physics Olympiads
**arXiv**：[2602.09443v1](https://arxiv.org/abs/2602.09443) · [PDF](https://arxiv.org/pdf/2602.09443.pdf)  
**作者**：Yun Luo, Futing Wang, Qianjia Cheng, Fangchen Yu, Haodi Lei, Jianhao Yan, Chenxi Li, Jiacheng Chen, Yufeng Zhao, Haiyuan Wan, Yuchen Zhang, Shenghe Zheng, Junchi Yao, Qingyang Zhang, Haonan He, Wenxuan Zeng, Li Sheng, Chengxing Xie, Yuxin Zuo, Yizhuo Li, Yulun Wu, Rui Huang, Dongzhan Zhou, Kai Chen, Yu Qiao, Lei Bai, Yu Cheng, Ning Ding, Bowen Zhou, Peng Ye, Ganqu Cui  

**一句话要点**：提出P1-VL视觉语言模型以解决物理奥赛中视觉感知与科学推理的鸿沟

**关键词**：视觉语言模型, 科学推理, 物理奥赛, 课程强化学习, 智能体增强

## 3 点简述
- 核心问题：物理奥赛图表包含文本缺失的关键约束，需将抽象逻辑与现实物理规律对齐
- 方法要点：结合课程强化学习稳定训练与智能体增强实现推理时迭代自验证
- 实验或效果：在HiPhO基准上获12枚金牌，开源模型中性能最优，全球总排名第二

## 摘要（原文）

> The transition from symbolic manipulation to science-grade reasoning represents a pivotal frontier for Large Language Models (LLMs), with physics serving as the critical test anchor for binding abstract logic to physical reality. Physics demands that a model maintain physical consistency with the laws governing the universe, a task that fundamentally requires multimodal perception to ground abstract logic in reality. At the Olympiad level, diagrams are often constitutive rather than illustrative, containing essential constraints, such as boundary conditions and spatial symmetries, that are absent from the text. To bridge this visual-logical gap, we introduce P1-VL, a family of open-source vision-language models engineered for advanced scientific reasoning. Our method harmonizes Curriculum Reinforcement Learning, which employs progressive difficulty expansion to stabilize post-training, with Agentic Augmentation, enabling iterative self-verification at inference. Evaluated on HiPhO, a rigorous benchmark of 13 exams from 2024-2025, our flagship P1-VL-235B-A22B becomes the first open-source Vision-Language Model (VLM) to secure 12 gold medals and achieves the state-of-the-art performance in the open-source models. Our agent-augmented system achieves the No.2 overall rank globally, trailing only Gemini-3-Pro. Beyond physics, P1-VL demonstrates remarkable scientific reasoning capacity and generalizability, establishing significant leads over base models in STEM benchmarks. By open-sourcing P1-VL, we provide a foundational step toward general-purpose physical intelligence to better align visual perceptions with abstract physical laws for machine scientific discovery.

