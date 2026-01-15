---
layout: default
title: CogRail: Benchmarking VLMs in Cognitive Intrusion Perception for Intelligent Railway Transportation Systems
---

# CogRail: Benchmarking VLMs in Cognitive Intrusion Perception for Intelligent Railway Transportation Systems
**arXiv**：[2601.09613v1](https://arxiv.org/abs/2601.09613) · [PDF](https://arxiv.org/pdf/2601.09613.pdf)  
**作者**：Yonglin Tian, Qiyao Zhang, Wei Xu, Yutong Wang, Yihao Wu, Xinyi Li, Xingyuan Dai, Hui Zhang, Zhiyong Cui, Baoqing Guo, Zujun Yu, Yisheng Lv  

**一句话要点**：提出CogRail基准以解决铁路入侵感知中的时空认知推理问题

**关键词**：视觉语言模型, 时空推理, 入侵感知, 多任务学习, 铁路安全

## 3 点简述
- 现有系统依赖固定视觉范围分类和规则启发，难以感知潜在入侵风险
- 构建集成开源数据集和认知问答标注的基准，支持时空推理与预测
- 通过联合微调框架显著提升视觉语言模型在入侵感知任务中的性能

## 摘要（原文）

> Accurate and early perception of potential intrusion targets is essential for ensuring the safety of railway transportation systems. However, most existing systems focus narrowly on object classification within fixed visual scopes and apply rule-based heuristics to determine intrusion status, often overlooking targets that pose latent intrusion risks. Anticipating such risks requires the cognition of spatial context and temporal dynamics for the object of interest (OOI), which presents challenges for conventional visual models. To facilitate deep intrusion perception, we introduce a novel benchmark, CogRail, which integrates curated open-source datasets with cognitively driven question-answer annotations to support spatio-temporal reasoning and prediction. Building upon this benchmark, we conduct a systematic evaluation of state-of-the-art visual-language models (VLMs) using multimodal prompts to identify their strengths and limitations in this domain. Furthermore, we fine-tune VLMs for better performance and propose a joint fine-tuning framework that integrates three core tasks, position perception, movement prediction, and threat analysis, facilitating effective adaptation of general-purpose foundation models into specialized models tailored for cognitive intrusion perception. Extensive experiments reveal that current large-scale multimodal models struggle with the complex spatial-temporal reasoning required by the cognitive intrusion perception task, underscoring the limitations of existing foundation models in this safety-critical domain. In contrast, our proposed joint fine-tuning framework significantly enhances model performance by enabling targeted adaptation to domain-specific reasoning demands, highlighting the advantages of structured multi-task learning in improving both accuracy and interpretability. Code will be available at https://github.com/Hub-Tian/CogRail.

