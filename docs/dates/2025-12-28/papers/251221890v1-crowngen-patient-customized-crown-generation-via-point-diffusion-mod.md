---
layout: default
title: CrownGen: Patient-customized Crown Generation via Point Diffusion Model
---

# CrownGen: Patient-customized Crown Generation via Point Diffusion Model
**arXiv**：[2512.21890v1](https://arxiv.org/abs/2512.21890) · [PDF](https://arxiv.org/pdf/2512.21890.pdf)  
**作者**：Juyoung Bae, Moo Hyun Son, Jiale Peng, Wanting Qu, Wener Chen, Zelin Qiu, Kaixin Li, Xiaojuan Chen, Yifan Lin, Hao Chen  

**一句话要点**：提出CrownGen，通过点扩散模型自动化患者定制牙冠设计以解决修复牙科中的劳动密集型瓶颈。

**关键词**：牙冠生成, 点扩散模型, 牙齿级点云, 边界预测, 临床验证, 自动化设计

## 3 点简述
- 核心问题：数字牙冠设计在修复牙科中仍是劳动密集型瓶颈，需要自动化解决方案。
- 方法要点：使用去噪扩散模型在牙齿级点云表示上生成高保真形态，结合边界预测模块建立空间先验。
- 实验或效果：在496个外部扫描的定量基准和26个临床案例中验证，几何保真度超越现有模型，临床评估显示质量不劣于专家手动工作流。

## 摘要（原文）

> Digital crown design remains a labor-intensive bottleneck in restorative dentistry. We present \textbf{CrownGen}, a generative framework that automates patient-customized crown design using a denoising diffusion model on a novel tooth-level point cloud representation. The system employs two core components: a boundary prediction module to establish spatial priors and a diffusion-based generative module to synthesize high-fidelity morphology for multiple teeth in a single inference pass. We validated CrownGen through a quantitative benchmark on 496 external scans and a clinical study of 26 restoration cases. Results demonstrate that CrownGen surpasses state-of-the-art models in geometric fidelity and significantly reduces active design time. Clinical assessments by trained dentists confirmed that CrownGen-assisted crowns are statistically non-inferior in quality to those produced by expert technicians using manual workflows. By automating complex prosthetic modeling, CrownGen offers a scalable solution to lower costs, shorten turnaround times, and enhance patient access to high-quality dental care.

