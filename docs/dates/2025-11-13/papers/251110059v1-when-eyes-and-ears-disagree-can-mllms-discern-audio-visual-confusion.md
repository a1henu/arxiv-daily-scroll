---
layout: default
title: When Eyes and Ears Disagree: Can MLLMs Discern Audio-Visual Confusion?
---

# When Eyes and Ears Disagree: Can MLLMs Discern Audio-Visual Confusion?
**arXiv**：[2511.10059v1](https://arxiv.org/abs/2511.10059) · [PDF](https://arxiv.org/pdf/2511.10059.pdf)  
**作者**：Qilang Ye, Wei Zeng, Meng Liu, Jie Zhang, Yupeng Hu, Zitong Yu, Yu Zhou  

**一句话要点**：提出RL-CoMM以解决多模态大语言模型在视听混淆场景中的视觉主导推理问题

**关键词**：多模态大语言模型, 视听混淆, 强化学习, 音频语言模型, 基准测试, 推理优化

## 3 点简述
- 核心问题：MLLMs难以识别视觉存在但音频缺失的混淆对象，如静音物体
- 方法要点：引入外部音频模型和强化学习，分阶段优化视听推理与答案置信度
- 实验或效果：在基准测试中，RL-CoMM比基线模型准确率提升10~30%

## 摘要（原文）

> Can Multimodal Large Language Models (MLLMs) discern confused objects that are visually present but audio-absent? To study this, we introduce a new benchmark, AV-ConfuseBench, which simulates an ``Audio-Visual Confusion'' scene by modifying the corresponding sound of an object in the video, e.g., mute the sounding object and ask MLLMs Is there a/an muted-object sound''. Experimental results reveal that MLLMs, such as Qwen2.5-Omni and Gemini 2.5, struggle to discriminate non-existent audio due to visually dominated reasoning. Motivated by this observation, we introduce RL-CoMM, a Reinforcement Learning-based Collaborative Multi-MLLM that is built upon the Qwen2.5-Omni foundation. RL-CoMM includes two stages: 1) To alleviate visually dominated ambiguities, we introduce an external model, a Large Audio Language Model (LALM), as the reference model to generate audio-only reasoning. Then, we design a Step-wise Reasoning Reward function that enables MLLMs to self-improve audio-visual reasoning with the audio-only reference. 2) To ensure an accurate answer prediction, we introduce Answer-centered Confidence Optimization to reduce the uncertainty of potential heterogeneous reasoning differences. Extensive experiments on audio-visual question answering and audio-visual hallucination show that RL-CoMM improves the accuracy by 10~30\% over the baseline model with limited training data. Follow: https://github.com/rikeilong/AVConfusion.

