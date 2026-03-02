---
layout: default
title: Can Unified Generation and Understanding Models Maintain Semantic Equivalence Across Different Output Modalities?
---

# Can Unified Generation and Understanding Models Maintain Semantic Equivalence Across Different Output Modalities?
**arXiv**：[2602.23711v1](https://arxiv.org/abs/2602.23711) · [PDF](https://arxiv.org/pdf/2602.23711.pdf)  
**作者**：Hongbo Jiang, Jie Li, Yunhang Shen, Pingyang Dai, Xing Sun, Haoyu Cao, Liujuan Cao  

**一句话要点**：提出VGUBench框架以诊断统一多模态大语言模型在跨模态语义等价性上的性能崩溃问题

**关键词**：统一多模态大语言模型, 语义等价性, 跨模态对齐, VGUBench框架, 视觉生成理解, 诊断评估

## 3 点简述
- 核心问题：现有统一多模态大语言模型在文本推理中表现稳健，但在生成图像模态答案时无法保持语义等价性
- 方法要点：引入VGUBench框架，通过文本生成理解、视觉生成理解和视觉渲染控制三个任务解耦推理逻辑与生成保真度
- 实验或效果：评估显示模型在视觉回答任务中性能显著下降，且视觉回答性能与基本渲染质量相关性可忽略，表明失败源于跨模态语义对齐崩溃

## 摘要（原文）

> Unified Multimodal Large Language Models (U-MLLMs) integrate understanding and generation within a single architecture. However, existing evaluations typically assess these capabilities separately, overlooking semantic equivalence, i.e., the ability to manifest consistent reasoning results regardless of the output modality. In this work, we investigate whether current U-MLLMs satisfy this premise. We observe that while models demonstrate robust textual reasoning, they fail to maintain semantic equivalence when required to render the same results in the image modality. To rigorously diagnose this discrepancy, we introduce VGUBench, a framework to decouple reasoning logic from generation fidelity. VGUBench comprises three diagnostic tasks: (1)Textual Generative Understanding, establishing a baseline for reasoning accuracy in textual response; (2)Visual Generative Understanding, evaluating the ability to generate visual responses that represent the correct answer; and (3)a Visual Rendering control task, which assesses the ability to directly render explicit visual descriptions into images without complex reasoning. Our evaluation reveals a significant disparity: despite strong performance in textual understanding and visual rendering, U-MLLMs exhibit a marked performance collapse when required to generate visual answers to questions. Furthermore, we find a negligible correlation between visual answering performance and basic rendering quality. These results suggest that the failure stems not from insufficient generation fidelity, but from a breakdown in cross-modal semantic alignment. We provide diagnostic insights to address this challenge in future Unified Generation and Understanding Models.

