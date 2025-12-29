---
layout: default
title: Look Closer! An Adversarial Parametric Editing Framework for Hallucination Mitigation in VLMs
---

# Look Closer! An Adversarial Parametric Editing Framework for Hallucination Mitigation in VLMs
**arXiv**：[2512.21999v1](https://arxiv.org/abs/2512.21999) · [PDF](https://arxiv.org/pdf/2512.21999.pdf)  
**作者**：Jiayu Hu, Beibei Li, Jiangwei Xia, Yanjun Qin, Bing Ji, Zhongshi He  

**一句话要点**：提出对抗性参数编辑框架ALEAHallu以缓解视觉语言模型中的幻觉问题

**关键词**：视觉语言模型, 幻觉缓解, 对抗性训练, 参数编辑, 视觉特征整合

## 3 点简述
- 核心问题：视觉语言模型因过度依赖语言先验和视觉特征整合不足而产生幻觉输出
- 方法要点：采用激活-定位-编辑对抗范式，通过对抗性前缀微调关键参数簇以增强视觉证据
- 实验或效果：在生成性和判别性任务上评估，显著减轻幻觉，代码已开源

## 摘要（原文）

> While Vision-Language Models (VLMs) have garnered increasing attention in the AI community due to their promising practical applications, they exhibit persistent hallucination issues, generating outputs misaligned with visual inputs. Recent studies attribute these hallucinations to VLMs' over-reliance on linguistic priors and insufficient visual feature integration, proposing heuristic decoding calibration strategies to mitigate them. However, the non-trainable nature of these strategies inherently limits their optimization potential. To this end, we propose an adversarial parametric editing framework for Hallucination mitigation in VLMs, which follows an \textbf{A}ctivate-\textbf{L}ocate-\textbf{E}dit \textbf{A}dversarially paradigm. Specifically, we first construct an activation dataset that comprises grounded responses (positive samples attentively anchored in visual features) and hallucinatory responses (negative samples reflecting LLM prior bias and internal knowledge artifacts). Next, we identify critical hallucination-prone parameter clusters by analyzing differential hidden states of response pairs. Then, these clusters are fine-tuned using prompts injected with adversarial tuned prefixes that are optimized to maximize visual neglect, thereby forcing the model to prioritize visual evidence over inherent parametric biases. Evaluations on both generative and discriminative VLM tasks demonstrate the significant effectiveness of ALEAHallu in alleviating hallucinations. Our code is available at https://github.com/hujiayu1223/ALEAHallu.

