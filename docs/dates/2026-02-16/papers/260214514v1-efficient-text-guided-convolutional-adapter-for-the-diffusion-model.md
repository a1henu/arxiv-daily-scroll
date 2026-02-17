---
layout: default
title: Efficient Text-Guided Convolutional Adapter for the Diffusion Model
---

# Efficient Text-Guided Convolutional Adapter for the Diffusion Model
**arXiv**：[2602.14514v1](https://arxiv.org/abs/2602.14514) · [PDF](https://arxiv.org/pdf/2602.14514.pdf)  
**作者**：Aryan Das, Koushik Biswas, Swalpa Kumar Roy, Badri Narayana Patro, Vinay Kumar Verma  

**一句话要点**：提出Nexus适配器以解决扩散模型中结构保持条件生成的效率与提示感知问题

**关键词**：扩散模型, 结构保持生成, 文本引导适配器, 多模态条件, 参数效率, 图像生成

## 3 点简述
- 现有结构保持方法效率低，适配器参数多且不感知输入提示
- Nexus适配器通过交叉注意力机制实现提示与结构输入的多模态引导
- Nexus Prime仅需8M额外参数，Nexus Slim参数更少且性能领先

## 摘要（原文）

> We introduce the Nexus Adapters, novel text-guided efficient adapters to the diffusion-based framework for the Structure Preserving Conditional Generation (SPCG). Recently, structure-preserving methods have achieved promising results in conditional image generation by using a base model for prompt conditioning and an adapter for structure input, such as sketches or depth maps. These approaches are highly inefficient and sometimes require equal parameters in the adapter compared to the base architecture. It is not always possible to train the model since the diffusion model is itself costly, and doubling the parameter is highly inefficient. In these approaches, the adapter is not aware of the input prompt; therefore, it is optimal only for the structural input but not for the input prompt. To overcome the above challenges, we proposed two efficient adapters, Nexus Prime and Slim, which are guided by prompts and structural inputs. Each Nexus Block incorporates cross-attention mechanisms to enable rich multimodal conditioning. Therefore, the proposed adapter has a better understanding of the input prompt while preserving the structure. We conducted extensive experiments on the proposed models and demonstrated that the Nexus Prime adapter significantly enhances performance, requiring only 8M additional parameters compared to the baseline, T2I-Adapter. Furthermore, we also introduced a lightweight Nexus Slim adapter with 18M fewer parameters than the T2I-Adapter, which still achieved state-of-the-art results. Code: https://github.com/arya-domain/Nexus-Adapters

