---
layout: default
title: LDP: Parameter-Efficient Fine-Tuning of Multimodal LLM for Medical Report Generation
---

# LDP: Parameter-Efficient Fine-Tuning of Multimodal LLM for Medical Report Generation
**arXiv**：[2512.10750v1](https://arxiv.org/abs/2512.10750) · [PDF](https://arxiv.org/pdf/2512.10750.pdf)  
**作者**：Tianyu Zhou, Junyi Tang, Zehui Li, Dahong Qian, Suncheng Xiang  

**一句话要点**：提出LDP框架，利用参数高效微调的多模态大语言模型解决结肠镜息肉诊断报告生成中的不一致和幻觉问题。

**关键词**：多模态大语言模型, 参数高效微调, 医学报告生成, 结肠镜诊断, 直接偏好优化, 数据集构建

## 3 点简述
- 核心问题：传统自动化报告因高质量多模态医疗数据稀缺导致不一致和幻觉，影响结肠镜息肉诊断。
- 方法要点：基于Qwen2-VL-7B，采用LoRA进行参数高效微调，并通过DPO与临床标准对齐，构建MMEndo数据集。
- 实验或效果：在自动指标和临床专家评估中优于基线，医师评分达7.2/10，训练计算成本比全微调降低833倍。

## 摘要（原文）

> Colonoscopic polyp diagnosis is pivotal for early colorectal cancer detection, yet traditional automated reporting suffers from inconsistencies and hallucinations due to the scarcity of high-quality multimodal medical data. To bridge this gap, we propose LDP, a novel framework leveraging multimodal large language models (MLLMs) for professional polyp diagnosis report generation. Specifically, we curate MMEndo, a multimodal endoscopic dataset comprising expert-annotated colonoscopy image-text pairs. We fine-tune the Qwen2-VL-7B backbone using Parameter-Efficient Fine-Tuning (LoRA) and align it with clinical standards via Direct Preference Optimization (DPO). Extensive experiments show that our LDP outperforms existing baselines on both automated metrics and rigorous clinical expert evaluations (achieving a Physician Score of 7.2/10), significantly reducing training computational costs by 833x compared to full fine-tuning. The proposed solution offers a scalable, clinically viable path for primary healthcare, with additional validation on the IU-XRay dataset confirming its robustness.

