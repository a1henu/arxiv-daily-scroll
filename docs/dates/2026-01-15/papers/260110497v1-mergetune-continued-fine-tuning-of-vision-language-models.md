---
layout: default
title: mergetune: Continued fine-tuning of vision-language models
---

# mergetune: Continued fine-tuning of vision-language models
**arXiv**：[2601.10497v1](https://arxiv.org/abs/2601.10497) · [PDF](https://arxiv.org/pdf/2601.10497.pdf)  
**作者**：Wenqing Wang, Da Li, Xiatian Zhu, Josef Kittler  

**一句话要点**：提出MERGETUNE方法，通过继续微调恢复视觉语言模型在适应后丢失的预训练知识。

**关键词**：视觉语言模型, 继续微调, 灾难性遗忘, 线性模式连通性, 模型合并, 零样本学习

## 3 点简述
- 核心问题：视觉语言模型微调常导致灾难性遗忘，现有方法难以完全避免。
- 方法要点：基于线性模式连通性，继续微调可训练参数，寻找连接零样本和微调模型的低损失路径。
- 实验或效果：在基础-新类别泛化上提升CoOp的调和平均5.6%，无需额外参数，并在跨数据集转移中超越CLIP。

## 摘要（原文）

> Fine-tuning vision-language models (VLMs) such as CLIP often leads to catastrophic forgetting of pretrained knowledge. Prior work primarily aims to mitigate forgetting during adaptation; however, forgetting often remains inevitable during this process. We introduce a novel paradigm, \emph{continued fine-tuning (CFT)}, which seeks to recover pretrained knowledge after a zero-shot model has already been adapted. We propose a simple, model-agnostic CFT strategy (named MERGETUNE) guided by linear mode connectivity (LMC), which can be applied post hoc to existing fine-tuned models without requiring architectural changes. Given a fine-tuned model, we continue fine-tuning its trainable parameters (e.g., soft prompts or linear heads) to search for a continued model which has two low-loss paths to the zero-shot (e.g., CLIP) and the fine-tuned (e.g., CoOp) solutions. By exploiting the geometry of the loss landscape, the continued model implicitly merges the two solutions, restoring pretrained knowledge lost in the fine-tuned counterpart. A challenge is that the vanilla LMC constraint requires data replay from the pretraining task. We approximate this constraint for the zero-shot model via a second-order surrogate, eliminating the need for large-scale data replay. Experiments show that MERGETUNE improves the harmonic mean of CoOp by +5.6\% on base-novel generalisation without adding parameters. % We show \emph{the first time} superior performance than CLIP on both DTD and EuroSAT, on cross-dataset transfer. On robust fine-tuning evaluations, the LMC-merged model from MERGETUNE surpasses ensemble baselines with lower inference cost, achieving further gains and state-of-the-art results when ensembled with the zero-shot model. Our code is available at \href{https://github.com/Surrey-UP-Lab/MERGETUNE}{https://github.com/Surrey-UP-Lab/MERGETUNE}.

