---
layout: default
title: When Does Multimodal Learning Help in Healthcare? A Benchmark on EHR and Chest X-Ray Fusion
---

# When Does Multimodal Learning Help in Healthcare? A Benchmark on EHR and Chest X-Ray Fusion
**arXiv**：[2602.23614v1](https://arxiv.org/abs/2602.23614) · [PDF](https://arxiv.org/pdf/2602.23614.pdf)  
**作者**：Kejing Yin, Haizhou Xu, Wenfang Yao, Chen Liu, Zijie Chen, Yui Haang Cheung, William K. Cheung, Jing Qin  

**一句话要点**：系统评估EHR与CXR多模态融合在临床预测中的有效性、鲁棒性与公平性

**关键词**：多模态学习, 电子健康记录, 胸部X光, 临床预测, 模态缺失, 算法公平性

## 3 点简述
- 核心问题：探究多模态学习在医疗实践中何时有效，特别是在模态缺失和公平性约束下
- 方法要点：基于MIMIC-IV和MIMIC-CXR标准化队列，系统比较不同融合策略并分析模态不平衡影响
- 实验或效果：发现多模态融合在模态完整时提升性能，但缺失时需专门设计，且不自动改善公平性

## 摘要（原文）

> Machine learning holds promise for advancing clinical decision support, yet it remains unclear when multimodal learning truly helps in practice, particularly under modality missingness and fairness constraints. In this work, we conduct a systematic benchmark of multimodal fusion between Electronic Health Records (EHR) and chest X-rays (CXR) on standardized cohorts from MIMIC-IV and MIMIC-CXR, aiming to answer four fundamental questions: when multimodal fusion improves clinical prediction, how different fusion strategies compare, how robust existing methods are to missing modalities, and whether multimodal models achieve algorithmic fairness. Our study reveals several key insights. Multimodal fusion improves performance when modalities are complete, with gains concentrating in diseases that require complementary information from both EHR and CXR. While cross-modal learning mechanisms capture clinically meaningful dependencies beyond simple concatenation, the rich temporal structure of EHR introduces strong modality imbalance that architectural complexity alone cannot overcome. Under realistic missingness, multimodal benefits rapidly degrade unless models are explicitly designed to handle incomplete inputs. Moreover, multimodal fusion does not inherently improve fairness, with subgroup disparities mainly arising from unequal sensitivity across demographic groups. To support reproducible and extensible evaluation, we further release a flexible benchmarking toolkit that enables plug-and-play integration of new models and datasets. Together, this work provides actionable guidance on when multimodal learning helps, when it fails, and why, laying the foundation for developing clinically deployable multimodal systems that are both effective and reliable. The open-source toolkit can be found at https://github.com/jakeykj/CareBench.

