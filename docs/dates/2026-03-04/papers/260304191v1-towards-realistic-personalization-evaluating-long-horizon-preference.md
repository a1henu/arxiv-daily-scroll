---
layout: default
title: Towards Realistic Personalization: Evaluating Long-Horizon Preference Following in Personalized User-LLM Interactions
---

# Towards Realistic Personalization: Evaluating Long-Horizon Preference Following in Personalized User-LLM Interactions
**arXiv**：[2603.04191v1](https://arxiv.org/abs/2603.04191) · [PDF](https://arxiv.org/pdf/2603.04191.pdf)  
**作者**：Qianyun Guo, Yibo Li, Yue Liu, Bryan Hooi  

**一句话要点**：提出RealPref基准以评估个性化用户-LLM交互中的长时偏好跟随能力

**关键词**：个性化LLM交互, 偏好跟随评估, 长时交互基准, 用户偏好建模, LLM-as-a-judge

## 3 点简述
- 核心问题：LLMs在现实长时交互中跟随用户偏好的能力评估不足
- 方法要点：构建包含用户档案、偏好表达类型和长时历史的基准RealPref
- 实验或效果：LLM性能随上下文增长和偏好隐式化而下降，泛化到未见场景具挑战

## 摘要（原文）

> Large Language Models (LLMs) are increasingly serving as personal assistants, where users share complex and diverse preferences over extended interactions. However, assessing how well LLMs can follow these preferences in realistic, long-term situations remains underexplored. This work proposes RealPref, a benchmark for evaluating realistic preference-following in personalized user-LLM interactions. RealPref features 100 user profiles, 1300 personalized preferences, four types of preference expression (ranging from explicit to implicit), and long-horizon interaction histories. It includes three types of test questions (multiple-choice, true-or-false, and open-ended), with detailed rubrics for LLM-as-a-judge evaluation. Results indicate that LLM performance significantly drops as context length grows and preference expression becomes more implicit, and that generalizing user preference understanding to unseen scenarios poses further challenges. RealPref and these findings provide a foundation for future research to develop user-aware LLM assistants that better adapt to individual needs. The code is available at https://github.com/GG14127/RealPref.

