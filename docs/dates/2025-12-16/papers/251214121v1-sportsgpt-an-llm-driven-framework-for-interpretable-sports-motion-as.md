---
layout: default
title: SportsGPT: An LLM-driven Framework for Interpretable Sports Motion Assessment and Training Guidance
---

# SportsGPT: An LLM-driven Framework for Interpretable Sports Motion Assessment and Training Guidance
**arXiv**：[2512.14121v1](https://arxiv.org/abs/2512.14121) · [PDF](https://arxiv.org/pdf/2512.14121.pdf)  
**作者**：Wenbo Tian, Ruting Lin, Hongxian Zheng, Yaodong Yang, Geng Wu, Zihao Zhang, Zhang Zhang  

**一句话要点**：提出SportsGPT框架，基于LLM实现可解释的运动评估与训练指导，解决现有系统缺乏自动诊断的问题。

**关键词**：运动分析, 大语言模型, 时间序列对齐, 可解释评估, 检索增强生成, 训练指导

## 3 点简述
- 现有智能运动分析系统主要关注评分与可视化，缺乏自动性能诊断和可解释的训练指导。
- 引入MotionDTW算法提取关键帧，设计KISMAM模型进行可解释评估，并基于SportsRAG生成专业训练指导。
- 实验表明MotionDTW优于传统方法，SportsGPT在诊断准确性和专业性上超越通用LLM。

## 摘要（原文）

> Existing intelligent sports analysis systems mainly focus on "scoring and visualization," often lacking automatic performance diagnosis and interpretable training guidance. Recent advances of Large Language Models (LMMs) and motion analysis techniques provide new opportunities to address the above limitations. In this paper, we propose SportsGPT, an LLM-driven framework for interpretable sports motion assessment and training guidance, which establishes a closed loop from motion time-series input to professional training guidance. First, given a set of high-quality target models, we introduce MotionDTW, a two-stage time series alignment algorithm designed for accurate keyframe extraction from skeleton-based motion sequences. Subsequently, we design a Knowledge-based Interpretable Sports Motion Assessment Model (KISMAM) to obtain a set of interpretable assessment metrics (e.g., insufficient extension) by constrasting the keyframes with the targe models. Finally, we propose SportsRAG, a RAG-based training guidance model based on Qwen3. Leveraging a 6B-token knowledge base, it prompts the LLM to generate professional training guidance by retrieving domain-specific QA pairs. Experimental results demonstrate that MotionDTW significantly outperforms traditional methods with lower temporal error and higher IoU scores. Furthermore, ablation studies validate the KISMAM and SportsRAG, confirming that SportsGPT surpasses general LLMs in diagnostic accuracy and professionalism.

