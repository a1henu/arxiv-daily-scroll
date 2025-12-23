---
layout: default
title: PENDULUM: A Benchmark for Assessing Sycophancy in Multimodal Large Language Models
---

# PENDULUM: A Benchmark for Assessing Sycophancy in Multimodal Large Language Models
**arXiv**：[2512.19350v1](https://arxiv.org/abs/2512.19350) · [PDF](https://arxiv.org/pdf/2512.19350.pdf)  
**作者**：A. B. M. Ashikur Rahman, Saeed Anwar, Muhammad Usman, Irfan Ahmad, Ajmal Mian  

**一句话要点**：提出PENDULUM基准以评估多模态大语言模型中的谄媚行为

**关键词**：多模态大语言模型, 谄媚行为评估, 视觉问答基准, 事实一致性, 模型鲁棒性, 幻觉检测

## 3 点简述
- 核心问题：多模态大语言模型存在谄媚行为，即过度迎合用户输入而牺牲事实准确性或视觉证据
- 方法要点：构建包含约2000个人工标注视觉问答对的基准，覆盖六种图像领域以系统研究谄媚倾向
- 实验或效果：评估显示模型鲁棒性差异大，易受谄媚和幻觉影响，并提出量化指标以深入分析

## 摘要（原文）

> Sycophancy, an excessive tendency of AI models to agree with user input at the expense of factual accuracy or in contradiction of visual evidence, poses a critical and underexplored challenge for multimodal large language models (MLLMs). While prior studies have examined this behavior in text-only settings of large language models, existing research on visual or multimodal counterparts remains limited in scope and depth of analysis. To address this gap, we introduce a comprehensive evaluation benchmark, \textit{PENDULUM}, comprising approximately 2,000 human-curated Visual Question Answering pairs specifically designed to elicit sycophantic responses. The benchmark spans six distinct image domains of varying complexity, enabling a systematic investigation of how image type and inherent challenges influence sycophantic tendencies. Through extensive evaluation of state-of-the-art MLLMs. we observe substantial variability in model robustness and a pronounced susceptibility to sycophantic and hallucinatory behavior. Furthermore, we propose novel metrics to quantify sycophancy in visual reasoning, offering deeper insights into its manifestations across different multimodal contexts. Our findings highlight the urgent need for developing sycophancy-resilient architectures and training strategies to enhance factual consistency and reliability in future MLLMs. Our proposed dataset with MLLMs response are available at https://github.com/ashikiut/pendulum/.

