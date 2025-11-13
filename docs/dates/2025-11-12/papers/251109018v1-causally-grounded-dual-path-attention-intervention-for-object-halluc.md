---
layout: default
title: Causally-Grounded Dual-Path Attention Intervention for Object Hallucination Mitigation in LVLMs
---

# Causally-Grounded Dual-Path Attention Intervention for Object Hallucination Mitigation in LVLMs
**arXiv**：[2511.09018v1](https://arxiv.org/abs/2511.09018) · [PDF](https://arxiv.org/pdf/2511.09018.pdf)  
**作者**：Liu Yu, Zhonghao Chen, Ping Kuang, Zhikun Feng, Fan Zhou, Lan Wang, Gillian Dobbie  

**一句话要点**：提出Owl框架以缓解大型视觉语言模型中的物体幻觉问题

**关键词**：物体幻觉缓解, 视觉语言模型, 注意力干预, 因果建模, 对比解码, VTACR指标

## 3 点简述
- 核心问题：物体幻觉导致模型生成与视觉输入不一致的内容
- 方法要点：基于因果图建模，引入VTACR指标和双路径注意力干预机制
- 实验或效果：在POPE和CHAIR基准上显著减少幻觉，保持视觉语言理解能力

## 摘要（原文）

> Object hallucination remains a critical challenge in Large Vision-Language Models (LVLMs), where models generate content inconsistent with visual inputs. Existing language-decoder based mitigation approaches often regulate visual or textual attention independently, overlooking their interaction as two key causal factors. To address this, we propose Owl (Bi-mOdal attention reWeighting for Layer-wise hallucination mitigation), a causally-grounded framework that models hallucination process via a structural causal graph, treating decomposed visual and textual attentions as mediators. We introduce VTACR (Visual-to-Textual Attention Contribution Ratio), a novel metric that quantifies the modality contribution imbalance during decoding. Our analysis reveals that hallucinations frequently occur in low-VTACR scenarios, where textual priors dominate and visual grounding is weakened. To mitigate this, we design a fine-grained attention intervention mechanism that dynamically adjusts token- and layer-wise attention guided by VTACR signals. Finally, we propose a dual-path contrastive decoding strategy: one path emphasizes visually grounded predictions, while the other amplifies hallucinated ones -- letting visual truth shine and hallucination collapse. Experimental results on the POPE and CHAIR benchmarks show that Owl achieves significant hallucination reduction, setting a new SOTA in faithfulness while preserving vision-language understanding capability. Our code is available at https://github.com/CikZ2023/OWL

