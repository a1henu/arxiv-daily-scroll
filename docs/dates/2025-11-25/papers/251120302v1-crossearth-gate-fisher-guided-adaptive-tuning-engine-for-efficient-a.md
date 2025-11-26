---
layout: default
title: CrossEarth-Gate: Fisher-Guided Adaptive Tuning Engine for Efficient Adaptation of Cross-Domain Remote Sensing Semantic Segmentation
---

# CrossEarth-Gate: Fisher-Guided Adaptive Tuning Engine for Efficient Adaptation of Cross-Domain Remote Sensing Semantic Segmentation
**arXiv**：[2511.20302v1](https://arxiv.org/abs/2511.20302) · [PDF](https://arxiv.org/pdf/2511.20302.pdf)  
**作者**：Shilei Cao, Ziyang Gong, Hehai Lin, Yang Liu, Jiashun Cheng, Xiaoxing Hu, Haoyuan Liang, Guowen Li, Chengwei Qin, Hong Cheng, Xue Yang, Juepeng Zheng, Haohuan Fu  

**一句话要点**：提出CrossEarth-Gate以解决遥感跨域语义分割中的多面域差距问题

**关键词**：遥感语义分割, 参数高效微调, 跨域适应, Fisher信息, 动态模块选择, 多面域差距

## 3 点简述
- 核心问题：现有参数高效微调方法难以处理遥感数据中的空间、语义和频率域差距
- 方法要点：构建多模块工具箱，并基于Fisher信息动态选择关键模块进行激活
- 实验或效果：在16个跨域基准测试中达到最优性能，验证了方法的有效性和泛化性

## 摘要（原文）

> In Remote Sensing (RS), Parameter-Efficient Fine-Tuning (PEFT) has emerged as a key approach to activate the generalizable representation ability of foundation models for downstream tasks. However, existing specialized PEFT methods often fail when applied to large-scale Earth observation tasks, as they are unable to fully handle the multifaceted and unpredictable domain gaps (\eg, spatial, semantic, and frequency shifts) inherent in RS data. To overcome this, we propose CrossEarth-Gate, which introduces two primary contributions. First, we establish a comprehensive RS module toolbox to address multifaceted domain gaps, comprising spatial, semantic, and frequency modules. Second, we develop a Fisher-guided adaptive selection mechanism that operates on this toolbox. This selection is guided by Fisher Information to quantify each module's importance by measuring its contribution to the task-specific gradient flow. It dynamically activates only the most critical modules at the appropriate layers, guiding the gradient flow to maximize adaptation effectiveness and efficiency. Comprehensive experiments validate the efficacy and generalizability of our method, where CrossEarth-Gate achieves state-of-the-art performance across 16 cross-domain benchmarks for RS semantic segmentation. The code of the work will be released.

